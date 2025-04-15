from odoo import models, fields, api
import requests
import base64

class MayanDocument(models.Model):
    _name = 'mayan.document'
    _description = 'Mayan EDMS Document'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Document Name', required=True, tracking=True)
    mayan_id = fields.Char(string='Mayan Document ID', required=True)
    document_type = fields.Char(string='Document Type')
    content = fields.Text(string='Document Content')
    file_name = fields.Char(string='File Name')
    file_data = fields.Binary(string='Document File')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('processed', 'Processed'),
        ('error', 'Error')
    ], default='draft', tracking=True)
    
    @api.model
    def sync_from_mayan(self):
        """Synchronize documents from Mayan EDMS"""
        ICPSudo = self.env['ir.config_parameter'].sudo()
        mayan_url = ICPSudo.get_param('mayan_integration.url')
        mayan_token = ICPSudo.get_param('mayan_integration.api_token')

        if not mayan_url or not mayan_token:
            return False

        headers = {
            'Authorization': f'Token {mayan_token}',
            'Accept': 'application/json',
        }

        try:
            # Get documents from Mayan EDMS
            response = requests.get(f'{mayan_url}/api/v4/documents/', headers=headers)
            response.raise_for_status()
            documents = response.json()

            for doc in documents['results']:
                # Check if document already exists
                existing_doc = self.search([('mayan_id', '=', str(doc['id']))])
                if not existing_doc:
                    # Get document content
                    content_response = requests.get(
                        f'{mayan_url}/api/v4/documents/{doc["id"]}/versions/first/pages/1/content/',
                        headers=headers
                    )
                    content = content_response.json().get('content', '')

                    # Create new document record
                    self.create({
                        'name': doc['label'],
                        'mayan_id': str(doc['id']),
                        'document_type': doc['document_type']['label'],
                        'content': content,
                        'state': 'processed'
                    })

            return True
        except Exception as e:
            return False

    def action_process_document(self):
        """Process document content using existing AI tools"""
        from utils.mayan_loader import MayanOCRLoader
        for record in self:
            try:
                # Create temporary file for processing
                import tempfile
                import base64
                import os

                if not record.file_data:
                    raise Exception('No file data to process')

                with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(record.file_name)[1]) as temp_file:
                    temp_file.write(base64.b64decode(record.file_data))
                    temp_file_path = temp_file.name

                # Process using existing OCR system
                ocr_loader = MayanOCRLoader(temp_file_path)
                documents = ocr_loader.load()

                if documents:
                    # Update document content with OCR results
                    record.content = documents[0].page_content
                    record.state = 'processed'
                    record.message_post(body='Document successfully processed with OCR')
                else:
                    raise Exception('OCR processing returned no results')

                # Clean up temp file
                os.unlink(temp_file_path)

            except Exception as e:
                record.state = 'error'
                record.message_post(body=f'Error processing document: {str(e)}')
