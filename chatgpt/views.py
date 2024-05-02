import json

import requests
from django.shortcuts import render

# Create your views here.
from django.http import StreamingHttpResponse, JsonResponse, request
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

# views.py


@csrf_exempt
def stream_completions(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user_message = data.get('message', '')
        print("User Message:", user_message)  # Add this line for debugging
        if user_message:

            # Send user message to GPT-3.5 and stream responses
            messages = [{"role": "user", "content": user_message}]
            # Assuming you have already initialized the OpenAI client
            # and assigned it to the variable `client`
            response = client.chat.completions.create(
                messages=messages,
                model="openai/gpt-3.5-turbo",
                stream=True
            )
            completion = ""
            for chunk in response:
                # print(chunk,"this is chunk")
                if chunk.choices:
                    for choice in chunk.choices:
                        completion += choice.delta.content
                        print(completion)

            return JsonResponse({'completion': completion})
        else:
            return JsonResponse({'error': 'Empty message'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)



# def stream_view(request):
#     return StreamingHttpResponse(stream_completions(), content_type='text/plain')

