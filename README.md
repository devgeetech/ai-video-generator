## Steps

1. `pip install "fastapi[all]"`
2. `pip install openai`
3. Set up `.env` and `config.py`
4. Setting up openai config
5. Setting up prompt to generate script and image prompts

```json
{
  "data": {
    "id": "chatcmpl-8IFP0nlDsjaKZo3h5ET60ZkIR6CvX",
    "choices": [
      {
        "finish_reason": "stop",
        "index": 0,
        "message": {
          "content": "{\n  \"script\": [\n    {\n      \"text\": \"Welcome to the world of Rust, the language for reliable and efficient software!\",\n      \"imagePrompt\": \"futuristic computer code with Rust logo\"\n    },\n    {\n      \"text\": \"Rust offers memory safety without a garbage collector.\",\n      \"imagePrompt\": \"illustration of a shield symbolizing safety with computer memory chips and the Rust logo\"\n    },\n    {\n      \"text\": \"Its rich type system prevents bugs at compile time.\",\n      \"imagePrompt\": \"a checkmark over a list of computer code bugs with a Rust compiler window in the background\"\n    },\n    {\n      \"text\": \"Concurrent programming is made easy with Rust's ownership model.\",\n      \"imagePrompt\": \"cartoon hands exchanging data packets labeled with Rust logo, symbolizing ownership model\"\n    },\n    {\n      \"text\": \"Start your journey with Rust and unlock high-performance applications.\",\n      \"imagePrompt\": \"a person opening a treasure chest glowing with light and the Rust logo inside symbolizing unlocking potential\"\n    }\n  ]\n}",
          "role": "assistant",
          "function_call": null,
          "tool_calls": null
        }
      }
    ],
    "created": 1699359802,
    "model": "gpt-4-1106-preview",
    "object": "chat.completion",
    "system_fingerprint": "fp_a24b4d720c",
    "usage": {
      "completion_tokens": 222,
      "prompt_tokens": 113,
      "total_tokens": 335
    }
  }
}
```

```json
{
  "data": {
    "videoScript": [
      {
        "text": "Dive into the deep blue and discover the world of dolphins.",
        "imagePrompt": "Underwater scene with dolphins swimming in the deep blue ocean"
      },
      {
        "text": "These intelligent creatures are known for their playfulness and agility.",
        "imagePrompt": "Dolphins leaping joyfully out of water"
      },
      {
        "text": "Dolphins communicate with each other through a series of clicks and whistles.",
        "imagePrompt": "Close-up of a dolphin emitting sound waves underwater"
      },
      {
        "text": "They live in social groups and often display signs of compassion and cooperation.",
        "imagePrompt": "A pod of dolphins swimming together showing cooperative behavior"
      },
      {
        "text": "Join us as we uncover the mysteries of these remarkable marine mammals.",
        "imagePrompt": "An over-shoulder shot of a diver observing dolphins in their natural habitat"
      }
    ]
  }
}
```
