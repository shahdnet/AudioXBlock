"""TO-DO: This XBlock will play an MP3 file as an HTML5 audio element. """

import pkg_resources

from django.template.loader import get_template
from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment


class AudioXBlock(XBlock):
    """
    This XBlock will play an MP3 file as an HTML5 audio element. 
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.
    src = String(
           scope = Scope.settings, 
           help = "URL for MP3 file to play"
        )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the AudioXBlock, shown to students
        when viewing courses.
        """
        context = {
            'src': self.src
        }
        frag = Fragment()
        frag.add_content(
            get_template(
                "audio.html"
            ).render( context )
        )
        frag.add_css(self.resource_string("static/css/audio.css"))
        return frag

    def studio_view(self, context):
        """
        The view for editing the AudioXBlock parameters inside Studio.
        """
        context = {
            'src': self.src
        }
        frag = Fragment()
        frag.add_content(
            get_template(
                "audio_edit.html"
            ).render( context )
        )

        js = self.resource_string("static/js/audio_edit.js")
        frag.add_javascript(js)
        frag.initialize_js('AudioEditBlock')

        return frag

    @XBlock.json_handler
    def studio_submit(self, data, suffix=''):
        """
        Called when submitting the form in Studio.
        """
        self.src = data.get('src')

        return {'result': 'success'}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("AudioXBlock",
             """<vertical_demo>
                  <audio src="http://localhost/Ikea.mp3"> </audio>
                  <audio src="http://localhost/skull.mp3"> </audio>
                  <audio src="http://localhost/monkey.mp3"> </audio>
                </vertical_demo>
             """),
        ]
