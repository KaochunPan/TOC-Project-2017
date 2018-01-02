from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_basic(self, update):
        text = update.message.text
        return text.lower() == 'basic'

    def is_going_to_crouched(self, update):
        text = update.message.text
        return text.lower() == 'crouched'

    def is_going_to_set_up(self, update):
        text = update.message.text
        return text.lower() == 'set_up'

    def is_going_to_spike(self, update):
        text = update.message.text
        return text.lower() == 'spike'

    def is_going_to_advanced(self, update):
        text = update.message.text
        return text.lower() == 'advanced'

    def is_going_to_defence(self, update):
        text = update.message.text
        return text.lower() == 'defence'

    def is_going_to_attack(self, update):
        text = update.message.text
        return text.lower() == 'attack'    

    def is_going_to_record(self, update):
        text = update.message.text
        return text.lower() == 'record'

    def is_going_to_year102(self, update):
        text = update.message.text
        return text.lower() == '102'

    def is_going_to_year103(self, update):
        text = update.message.text
        return text.lower() == '103'

    def is_going_to_year104(self, update):
        text = update.message.text
        return text.lower() == '104'

    def is_going_to_year105(self, update):
        text = update.message.text
        return text.lower() == '105'

    def on_enter_basic(self, update):
        update.message.reply_text("Welcome to the basic volleyball class!")
        update.message.reply_text("You can enter the following option:\n crouched\n set_up\n spike")

    def on_exit_basic(self, update):
        print('Leaving basic')

    def on_enter_crouched(self, update):
        update.message.reply_text("Now, introduce the coruched position")
        self.go_back(update)

    def on_exit_crouched(self, update):
        print('Leaving crouched')

    def on_enter_set_up(self, update):
        update.message.reply_text("Now, introduce the set up")
        self.go_back(update)

    def on_exit_set_up(self, update):
        print('Leaving set_up')

    def on_enter_spike(self, update):
        update.message.reply_text("Now, introduce the spike")
        self.go_back(update)

    def on_exit_spike(self, update):
        print('Leaving spike')

    def on_enter_advanced(self, update):
        update.message.reply_text("I'm entering advanced")

    def on_exit_advanced(self, update):
        print('Leaving advanced')

    def on_enter_defence(self, update):
        update.message.reply_text("I'm entering defence")
        self.go_back(update)

    def on_exit_defence(self, update):
        print('Leaving defence')

    def on_enter_attack(self, update):
        update.message.reply_text("I'm entering attack")
        self.go_back(update)

    def on_exit_attack(self, update):
        print('Leaving attack')

    def on_enter_record(self, update):
        update.message.reply_text("I'm entering record")
        update.message.reply_text("Please enter the year you want to search(102-105)")

    def on_exit_record(self, update):
        print('Leaving record')

    def on_enter_year102(self, update):
        update.message.reply_text("I'm entering year102")
        self.go_back(update)

    def on_exit_year102(self, update):
        print('Leaving year102')

    def on_enter_year103(self, update):
        update.message.reply_text("I'm entering year103")
        self.go_back(update)

    def on_exit_year103(self, update):
        print('Leaving year103')

    def on_enter_year104(self, update):
        update.message.reply_text("I'm entering year104")
        self.go_back(update)

    def on_exit_year104(self, update):
        print('Leaving year104')

    def on_enter_year105(self, update):
        update.message.reply_text("I'm entering year105")
        self.go_back(update)

    def on_exit_year105(self, update):
        print('Leaving year105')


