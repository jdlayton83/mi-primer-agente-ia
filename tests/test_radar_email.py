import os
import smtplib
import unittest
from types import SimpleNamespace
from unittest.mock import patch

os.environ.setdefault("GEMINI_API_KEY", "test-api-key")

import main


SMTP_SETTINGS = {
    "RADAR_SMTP_HOST": "smtp.example.com",
    "RADAR_SMTP_PORT": "587",
    "RADAR_SMTP_USER": "radar-user",
    "RADAR_SMTP_PASSWORD": "radar-password",
    "RADAR_SMTP_FROM": "radar@example.com",
    "RADAR_SMTP_TO": "recipient@example.com",
}


class RadarEmailTests(unittest.TestCase):
    def test_sends_message_using_starttls(self) -> None:
        with (
            patch.dict(os.environ, SMTP_SETTINGS, clear=True),
            patch("main.smtplib.SMTP") as smtp,
        ):
            server = smtp.return_value.__enter__.return_value

            main.enviar_resumen_por_correo("Resumen del radar")

            smtp.assert_called_once_with("smtp.example.com", 587, timeout=30)
            server.starttls.assert_called_once()
            server.login.assert_called_once_with("radar-user", "radar-password")
            sent_message = server.send_message.call_args.args[0]
            self.assertEqual(sent_message["From"], "radar@example.com")
            self.assertEqual(sent_message["To"], "recipient@example.com")
            self.assertEqual(sent_message.get_content(), "Resumen del radar\n")

    def test_port_465_uses_implicit_tls(self) -> None:
        settings = {**SMTP_SETTINGS, "RADAR_SMTP_PORT": "465"}
        with (
            patch.dict(os.environ, settings, clear=True),
            patch("main.smtplib.SMTP_SSL") as smtp_ssl,
        ):
            server = smtp_ssl.return_value.__enter__.return_value

            main.enviar_resumen_por_correo("Resumen del radar")

            smtp_ssl.assert_called_once()
            server.starttls.assert_not_called()
            server.login.assert_called_once_with("radar-user", "radar-password")
            server.send_message.assert_called_once()

    def test_missing_settings_fail_before_opening_smtp(self) -> None:
        with (
            patch.dict(os.environ, {}, clear=True),
            patch("main.smtplib.SMTP") as smtp,
        ):
            with self.assertRaisesRegex(ValueError, "RADAR_SMTP_HOST"):
                main.enviar_resumen_por_correo("Resumen del radar")

            smtp.assert_not_called()

    def test_missing_settings_prevent_gemini_request(self) -> None:
        with (
            patch.dict(os.environ, {"AGENT_SKILL": "radar_innovacion"}, clear=True),
            patch("main.generar_respuesta") as generate,
            patch("builtins.print"),
        ):
            with self.assertRaisesRegex(ValueError, "RADAR_SMTP_HOST"):
                main.ejecutar_agente()

            generate.assert_not_called()

    def test_smtp_errors_are_reported_without_server_details(self) -> None:
        with (
            patch.dict(os.environ, SMTP_SETTINGS, clear=True),
            patch("main.smtplib.SMTP") as smtp,
        ):
            server = smtp.return_value.__enter__.return_value
            server.starttls.side_effect = smtplib.SMTPAuthenticationError(
                535, b"private server detail"
            )

            with self.assertRaises(RuntimeError) as error:
                main.enviar_resumen_por_correo("Resumen del radar")

            self.assertIn("SMTPAuthenticationError", str(error.exception))
            self.assertNotIn("private server detail", str(error.exception))

    def test_generation_failure_does_not_send_email(self) -> None:
        environment = {
            **SMTP_SETTINGS,
            "AGENT_SKILL": "radar_innovacion",
        }
        with (
            patch.dict(os.environ, environment, clear=True),
            patch("main.cargar_hallazgos_rss", return_value=[]),
            patch("main.generar_respuesta", side_effect=RuntimeError("Gemini error")),
            patch("main.enviar_resumen_por_correo") as send_email,
            patch("builtins.print"),
        ):
            with self.assertRaisesRegex(RuntimeError, "Gemini error"):
                main.ejecutar_agente()

            send_email.assert_not_called()

    def test_successful_radar_generation_sends_email(self) -> None:
        environment = {
            **SMTP_SETTINGS,
            "AGENT_SKILL": "radar_innovacion",
        }
        with (
            patch.dict(os.environ, environment, clear=True),
            patch("main.cargar_hallazgos_rss", return_value=[]),
            patch("main.cargar_instruccion_sistema", return_value="system"),
            patch(
                "main.generar_respuesta",
                return_value=SimpleNamespace(text="Radar generado"),
            ),
            patch("main.enviar_resumen_por_correo") as send_email,
            patch("builtins.print"),
        ):
            main.ejecutar_agente()

            send_email.assert_called_once_with("Radar generado")


if __name__ == "__main__":
    unittest.main()
