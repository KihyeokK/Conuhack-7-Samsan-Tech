def detect_document(path):
    import cv2
    import os
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "put path here plz"
    diaryImage2 = cv2.imread(path)
    """Detects document features in an image."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)
    print(response.full_text_annotation.text)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    
    return response.full_text_annotation.text

def GPTchat(text):
  import openai

  # Replace "YOUR_API_KEY" with your OpenAI API key
  openai.api_key = "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"

  prompt = "in one word what is the emotion behind this text " + text

  # Generate a response from the model
  completions = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.7,
  )

  # Print the response
  response_text = completions.choices[0].text
  print(response_text)