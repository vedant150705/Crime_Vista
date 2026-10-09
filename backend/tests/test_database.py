import unittest

from app.database import _normalize_database_url


class DatabaseUrlTests(unittest.TestCase):
    def test_normalizes_render_postgres_url(self) -> None:
        self.assertEqual(
            _normalize_database_url("postgres://user:pass@db.example:5432/crimevista"),
            "postgresql+psycopg://user:pass@db.example:5432/crimevista",
        )

    def test_normalizes_postgresql_url_for_installed_driver(self) -> None:
        self.assertEqual(
            _normalize_database_url("postgresql://user:pass@db.example/crimevista"),
            "postgresql+psycopg://user:pass@db.example/crimevista",
        )

    def test_preserves_explicit_driver_and_non_postgres_urls(self) -> None:
        explicit_driver = "postgresql+psycopg://user:pass@db.example/crimevista"
        sqlite_url = "sqlite:///local.db"

        self.assertEqual(_normalize_database_url(explicit_driver), explicit_driver)
        self.assertEqual(_normalize_database_url(sqlite_url), sqlite_url)


if __name__ == "__main__":
    unittest.main()
