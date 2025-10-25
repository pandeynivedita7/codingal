import gradio as gr
def greet(name):
    return "welcome to @genai with Nivedita"+ name+" !"
demo =gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch(share=True)
