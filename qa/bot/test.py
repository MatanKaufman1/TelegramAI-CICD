import unittest
from unittest.mock import MagicMock
from qa_bot.app import Bot, QuoteBot, YoutubeBot


class TestBot(unittest.TestCase):

    def setUp(self):
        self.bot = Bot('test_token')

    def test_send_text(self):
        ## Mock the bot.send_message method and assert that it is called correctly
        self.bot.bot.send_message = MagicMock()
        self.bot.current_msg = MagicMock(chat=MagicMock(id=123))
        self.bot.send_text('Test message')
        self.bot.bot.send_message.assert_called_with(123, 'Test message')

    def test_send_text_with_quote(self):
        # Mock the bot.send_message method and assert that it is called correctly
        self.bot.bot.send_message = MagicMock()
        self.bot.current_msg = MagicMock(chat=MagicMock(id=123))
        self.bot.send_text_with_quote('Test message', 456)
        self.bot.bot.send_message.assert_called_with(123, 'Test message', reply_to_message_id=456)

    def test_is_current_msg_photo_with_photo(self):
        self.bot.current_msg = MagicMock(content_type='photo')
        self.assertTrue(self.bot.is_current_msg_photo())

class TestQuoteBot(unittest.TestCase):

    def setUp(self):
        self.bot = QuoteBot('test_token')

    def test_handle_message(self):
        # Mock the bot.send_text_with_quote method and assert that it is called correctly
        self.bot.send_text_with_quote = MagicMock()
        message = MagicMock(text='Test quote')
        self.bot.handle_message(message)
        self.bot.send_text_with_quote.assert_called_with('Test quote', message_id=message.message_id)

class TestYoutubeBot(unittest.TestCase):

    def setUp(self):
        self.bot = YoutubeBot('test_token')
        self.bot.current_msg = MagicMock()

    def test_handle_message_with_photo(self):
        # Mock the bot.download_user_photo method and assert its call
        self.bot.download_user_photo = MagicMock()
        self.bot.current_msg.content_type = 'photo'
        self.bot.handle_message(self.bot.current_msg)
        self.bot.download_user_photo.assert_called_with(quality=2)



if __name__ == '__main__':
    unittest.main()
