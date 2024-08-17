from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def setUp(self):
        """Setup before every test"""
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Test if homepage loads and displays on board."""
        with self.client:
            response = self.client.get('/')
            self.assertIn('board', session)
            self.assertIn(b'<div id="board">', response.data)


    def test_check_word(self):
        """Test if word checking functionality works."""
        with self.client as client:
            with client.session_transaction() as sess:
                sess['board'] = [["C", "A", "T", "T", "O"],
                             ["C", "M", "A", "T", "O"],
                             ["C", "A", "T", "T", "O"],
                             ["C", "A", "Y", "T", "O"],
                             ["C", "A", "T", "T", "O"]]
            response = client.get('/check-word?word=MATTY')
            self.assertEqual(response.json['result'], 'ok')