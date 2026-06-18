import os
import gradio as gr
import replicate

# 🔐 તમારી Replicate API Key અહીં સેટ કરો
# (પ્રોફેસનલ રીત: આને Render ના Environment Variables માં મુકવી, અથવા અત્યારે ટેસ્ટિંગ માટે અહીં ડાયરેક્ટ પેસ્ટ કરી શકો)
os.environ["REPLICATE_API_TOKEN"] = "r8_50mXTptCUQ6vNkz7darrmzmc06JMjMk1c0u4W"

print("🚀 API કનેક્શન સેટ થઈ ગયું છે. એપ લાઈવ થવા માટે રેડી છે!")

# ઇમેજ જનરેટ કરવાનું ફંક્શન (જે માત્ર ૨ સેકન્ડ લેશે)
def generate_ai_ad(prompt_text):
    # Replicate પર ફ્લક્સ મોડલને રન કમાન્ડ મોકલવો
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
    # output આપણને ઇમેજની ડાયરેક્ટ લિંક આપશે
    return output[0]

# ગ્રેડિયો સુંદર UI ડિઝાઇન
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🚀 BOULT AI Ad Generator Tool (Permanent Live)")
    gr.Markdown("તમારા પ્રોડક્ટ માટે પ્રીમિયમ સિનેમેટિક એડવર્ટાઇઝમેન્ટ ફોટોગ્રાફ્સ બનાવો - Powered by Replicate API.")
    
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

# Render ક્લાઉડ પર હોસ્ટ કરવા માટે આ લાઈન જરૂરી છે
demo.launch(server_name="0.0.0.0", server_port=7860)
