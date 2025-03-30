```
import unittest
from unittest.mock import MagicMock, patch

from src.cli.interface import display_tasks, get_user_input
from src.cli.menu import handle_menu_choice
from src.core.models import TaskList


class TestCLI(unittest.TestCase):
    def test_display_tasks_empty(self):
        with patch("builtins.print") as mock_print:
            display_tasks([])
            mock_print.assert_called_with("Nenhuma tarefa cadastrada.")

    @patch("builtins.input", side_effect=["test input"])
    def test_get_user_input_valid(self, mock_input):
        result = get_user_input("Prompt: ", lambda x: True)
        self.assertEqual(result, "test input")

    @patch("builtins.input", side_effect=["invalid", "2"])
    @patch("builtins.print")
    def test_get_user_input_with_validation(self, mock_print, mock_input):
        result = get_user_input("Prompt: ", lambda x: x == "2", "Erro")
        self.assertEqual(result, "2")
        mock_print.assert_called_with("Erro")


if __name__ == "__main__":
    unittest.main()

```
