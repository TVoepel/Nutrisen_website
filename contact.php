<?php
/**
 * NutriSen contact form handler (replaces the WordPress form backend of the old site).
 * Receives name, message and consent from assets/contact.js and sends them as one e-mail. Nothing is stored, no IP address is logged.
 *
 * Settings: TO is the receiving mailbox. FROM must be an address of a domain in your IONOS contract
 * (IONOS rejects other sender domains with "Sender address is not allowed").
 */
declare(strict_types=1);

const TO = 'info@nutrisen.eu';
const FROM = 'noreply@nutrisen.eu';
const MIN_MS = 3000;          // a human needs more than 3 seconds to fill in the form
const MAX_NAME = 200;
const MAX_MESSAGE = 2500;

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
header('X-Content-Type-Options: nosniff');

function done(int $status, array $body): void { http_response_code($status); echo json_encode($body); exit; }
function clean(string $s): string { return trim(str_replace(["\r", "\0"], '', $s)); }

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') done(405, ['ok' => false, 'error' => 'method']);

$name = clean((string)($_POST['name'] ?? ''));
$message = clean((string)($_POST['message'] ?? ''));
$consent = (string)($_POST['consent'] ?? '') === '1';
$lang = ((string)($_POST['lang'] ?? 'en')) === 'de' ? 'de' : 'en';
$elapsed = (int)($_POST['elapsed'] ?? 0);

if ((string)($_POST['website'] ?? '') !== '') done(200, ['ok' => true]);            // honeypot field filled in: a bot, pretend success
if ($elapsed < MIN_MS) done(429, ['ok' => false, 'error' => 'too_fast']);
if (!$consent || $name === '' || $message === '') done(422, ['ok' => false, 'error' => 'invalid']);
if (mb_strlen($name) > MAX_NAME || mb_strlen($message) > MAX_MESSAGE) done(422, ['ok' => false, 'error' => 'too_long']);

$subject = 'Anfrage über nutrisen.eu (' . strtoupper($lang) . ')';
$body = "Name: " . str_replace("\n", ' ', $name) . "\n\nNachricht:\n" . $message
      . "\n\n--\nDie Einwilligung zur Verarbeitung der Daten wurde im Formular erteilt.\nGesendet über das Kontaktformular auf nutrisen.eu\n";
$headers = [
    'From: NutriSen Website <' . FROM . '>',
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset=UTF-8',
    'Content-Transfer-Encoding: 8bit',
];
$ok = mail(TO, '=?UTF-8?B?' . base64_encode($subject) . '?=', $body, implode("\r\n", $headers));
done($ok ? 200 : 500, ['ok' => $ok]);
