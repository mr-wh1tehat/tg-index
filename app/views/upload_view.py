import logging

import aiohttp_jinja2

class UploadView:
    
    @aiohttp_jinja2.template("upload.html")
    async def upload_view(self, req):
        pass
