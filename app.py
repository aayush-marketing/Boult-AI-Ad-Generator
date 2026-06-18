import os
import gradio as gr
import replicate

# અહીં અંદર ટોકન લખવાની હવે કોઈ જરૂર નથી, Render તેને ઓટોમેટિક સિસ્ટમમાંથી ઉપાડી લેશે
# os.environ["REPLICATE_API_TOKEN"] = "..." 

def generate_ai_ad(prompt_text):
    output = replicate.run(
        "black-forest-labs/flux-schnell",
        input={
            "prompt": prompt_text,
            "go_fast": True,
            "megapixels": "1",
            "num_outputs": 1,
            "aspect_ratio": "1:1",
            "output_format": "webp",
            "output_quality": 80,
            "num_inference_steps": 4
        }
    )
    return output[0]

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🚀 BOULT AI Ad Generator Tool")
    
    with gr.Row():
        with gr.Column():
            user_input = gr.Textbox(
                label="તમારો પ્રોમ્પ્ટ અહીં લખો:", 
                value="A high-end cinematic advertisement photo of a luxury studio loft room. A beautiful model girl is sitting in an armchair on the left, reading a book. In the foreground, on a modern curved wooden table, premium sleek wireless neckband earbuds are placed under soft golden warm lighting. On the clean wall, 'BOULT: DEFINE YOUR VIBE' is written cleanly in a luxury font."
            )
            submit_btn = gr.Button("Generate Premium Ad ✨", variant="primary")
        with gr.Column():
            output_img = gr.Image(label="તમારી AI જનરેટેડ એડ")

    submit_btn.click(fn=generate_ai_ad, inputs=user_input, outputs=output_img)

demo.launch(server_name="0.0.0.0", server_port=7860)
