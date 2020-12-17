from mycroft import MycroftSkill, intent_file_handler


class TherapyMode(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('mode.therapy.intent')
    def handle_mode_therapy(self, message):
        self.speak_dialog('mode.therapy')


def create_skill():
    return TherapyMode()

