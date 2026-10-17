# Language Model

The Language Model application integrates FusionPBX with large or small
language models (LLMs). It provides a chat / assistant interface so an
administrator can talk to a model, attach an image to the prompt, and ask
the model to read a web page. It is an **AI** category application and is
available in FusionPBX 5.3.x and newer versions.

This is a language model (text) integration. For text-to-speech see
[Speech](speech.md) and for speech-to-text see
[Transcribe](transcribe.md).

The application is provided as a separate module that is installed on top
of a standard FusionPBX installation.

---

## Install

To use the Language Model application, install the module into the app
directory and register its permissions and default settings.

```
cd /var/www/fusionpbx/app
git clone https://github.com/fusionpbx/fusionpbx-app-language_model language_model
cd /var/www/fusionpbx
php core/upgrade/upgrade.php --permissions
php core/upgrade/upgrade.php --defaults
```

The `--permissions` step registers the **Applications → Language Model**
menu and its permissions, and the `--defaults` step registers the
`language_model` default settings described below.

After installing, go to **Advanced → Default Settings** and select the
**language_model** category to configure the engine.

---

## Upgrade

```
cd /var/www/fusionpbx/app/language_model
git pull
cd /var/www/fusionpbx
php core/upgrade/upgrade.php --permissions
php core/upgrade/upgrade.php --defaults
```

---

## Default Settings

Go to **Advanced → Default Settings** and use the drop-down filter to
select the **language_model** category. Make sure to set **enabled** to
true to use the application.

| Subcategory | Type | Default | Description |
|---|---|---|---|
| enabled | boolean | true (not enabled) | Language Model API enabled. |
| engine | text | ollama | Language Model engine. Options: ollama, openai, llama, local |
| api_key | text | | Language Model API key |
| api_url | text | | Language Model API URL |

The **openai** engine additionally reads an optional **api_model** setting
to select the model (default **o4-mini**); create that setting in the
**language_model** category to override the model.

---

## Engines

The **engine** setting selects which backend the application talks to. Only
the engines listed below are accepted; any other value is ignored, which
prevents a class being injected through the engine name.

**Ollama** (default) - Set engine to **ollama** and set the **api_url** to
the Ollama server (default http://127.0.0.1:11434). No API key is needed.
Pull a model first with `ollama pull <model>`; it then appears in the
model drop-down. The Ollama engine supports multi-message chat, tool
calling, extended "thinking", and streaming.

**OpenAI** - Set engine to **openai** and add the **api_key** (used as a
`Bearer` token). The **api_url** defaults to https://api.openai.com with
chat completions sent to
https://api.openai.com/v1/chat/completions. The model defaults to
**o4-mini**; set the optional **api_model** setting to use a different
model.

**llama** - Set engine to **llama** to use a local [llama.cpp](https://github.com/ggml-org/llama.cpp)
server that exposes an OpenAI-compatible API. Set the **api_url** to the
server (default http://127.0.0.1:8080). The list of models is read from
`/api/tags`, falling back to `/v1/models` on newer builds. Responses are
delivered as a server-sent event (SSE) stream.

**local** - Set engine to **local** to use a generic local endpoint. Set
the **api_url** to the server (default http://127.0.0.1:8787). The list of
models is read from `/models`.

---

## Usage

The Language Model page is available from **Applications → Language Model**
and requires the **language_model_view** permission (superadmin).

- Choose a model from the drop-down. The available models are read from the
  configured engine.
- Enter a prompt in the message box and press **Send**. The reply is
  streamed into the response pane as the model generates it.
- If the account has the **language_model_upload** permission, a paperclip
  (attach) button is shown. Use it to attach an image (PNG or JPG, up to
  10 MB) to the prompt so a vision-capable model can answer questions about
  it.

The response is delivered over a server-sent event (SSE) stream so the
reply appears word by word instead of waiting for the full response.

---

## Permissions

| Permission | Groups | Purpose |
|---|---|---|
| language_model_view | superadmin | Open the Language Model page |
| language_model_upload | superadmin | Attach an image to a prompt |

---

## Reading Web Pages

The model can be asked to read a web page referenced in the prompt. This is
off by default and is controlled by the config setting
`language_model.permissions.read.url` in `/etc/fusionpbx/fusionpbx.php`,
which defaults to **deny**. Set it to **allow** to enable URL reading.

When enabled, the application detects "read this page"-style intent and the
URL in the prompt (in a number of languages), fetches the page, and includes
its content for the model to answer from.

For safety the fetch is restricted:

- Only `http` and `https` URLs are fetched.
- Private and internal addresses are blocked (loopback, RFC 1918,
  `0.0.0.0/8`, `169.254/16`, and the equivalent IPv6 ranges).
- The page content is limited to 512 KB.
- DNS rebinding is prevented by re-resolving the host and fetching from the
  resolved address.

Debug messages are written to `/var/log/fusionpbx/language_model_debug.log`
(owner/group readable only).

---

## Chat API

Each engine is wrapped by a `language_model` class that dispatches to the
matching `language_model_<engine>` class. The public methods are:

- `get_models()` - returns the list of models available from the engine.
- `request($model, $content)` - sends a single prompt (optionally with
  attached images) and returns the model's text response.
- `chat($model, $messages, $tools, $opts)` - performs a multi-message chat
  with optional tool calling. It returns a structured result with `ok`,
  `content`, `tool_calls`, `thinking`, `prompt_tokens`, `completion_tokens`,
  `eval_duration`, `total_duration`, and `error`. Streaming and "thinking"
  are supported where the engine provides them (the Ollama engine does).

Other applications can use these methods to integrate the selected language
model.

---

## Related

- [Speech](speech.md) - text-to-speech
- [Transcribe](transcribe.md) - speech-to-text
