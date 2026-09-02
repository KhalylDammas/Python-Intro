"""Automated checks used during the Day 4 commit and PR demonstrations."""

import unittest

from team_greeting import WELCOME_MESSAGE, build_greeting


class BuildGreetingTests(unittest.TestCase):
    def test_uses_the_students_trimmed_name(self) -> None:
        self.assertEqual(
            build_greeting("  Sara  "),
            f"{WELCOME_MESSAGE} Hello, Sara.",
        )

    def test_uses_student_when_name_is_empty(self) -> None:
        self.assertEqual(
            build_greeting("   "),
            f"{WELCOME_MESSAGE} Hello, student.",
        )


if __name__ == "__main__":
    unittest.main()
