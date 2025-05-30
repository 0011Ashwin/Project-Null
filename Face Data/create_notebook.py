import json
import os

# Define the notebook content
notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Facial Emotion CNN Activation Maps Visualization\n",
                "\n",
                "This notebook demonstrates how to visualize activation maps from a CNN trained for facial emotion recognition."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import os\n",
                "import torch\n",
                "import numpy as np\n",
                "import matplotlib.pyplot as plt\n",
                "from PIL import Image\n",
                "import cv2\n",
                "import random\n",
                "\n",
                "# Import our activation map visualizer\n",
                "from visualize_activations import ActivationMapVisualizer"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Initialize the model\n",
                "model_path = \"model/emotion_model.pth\"  # Change if your model is elsewhere\n",
                "visualizer = ActivationMapVisualizer(model_path=model_path if os.path.exists(model_path) else None)\n",
                "\n",
                "# Create output directory\n",
                "output_dir = \"outputs\"\n",
                "if not os.path.exists(output_dir):\n",
                "    os.makedirs(output_dir)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Load a sample image\n",
                "# First try to find a real sample from the dataset\n",
                "sample_found = False\n",
                "emotions = ['happy', 'angry', 'disgust', 'fear', 'neutral', 'sad', 'surprise']\n",
                "\n",
                "# Try to find a sample in the train directory\n",
                "for emotion in emotions:\n",
                "    emotion_dir = os.path.join('train', emotion)\n",
                "    if os.path.exists(emotion_dir):\n",
                "        img_files = [f for f in os.listdir(emotion_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]\n",
                "        if img_files:\n",
                "            img_path = os.path.join(emotion_dir, img_files[0])\n",
                "            sample_found = True\n",
                "            print(f\"Found sample image: {img_path}\")\n",
                "            break\n",
                "\n",
                "# If no sample found in train, check test directory\n",
                "if not sample_found:\n",
                "    for emotion in emotions:\n",
                "        emotion_dir = os.path.join('test', emotion)\n",
                "        if os.path.exists(emotion_dir):\n",
                "            img_files = [f for f in os.listdir(emotion_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]\n",
                "            if img_files:\n",
                "                img_path = os.path.join(emotion_dir, img_files[0])\n",
                "                sample_found = True\n",
                "                print(f\"Found sample image: {img_path}\")\n",
                "                break\n",
                "\n",
                "# If still no sample found\n",
                "if not sample_found:\n",
                "    img_path = \"data/sample_face.jpg\"\n",
                "    print(\"No sample image found in dataset. Using default path which may not exist.\")\n",
                "\n",
                "# Display the original image\n",
                "if os.path.exists(img_path):\n",
                "    img = Image.open(img_path).convert(\"RGB\")\n",
                "    plt.figure(figsize=(6, 6))\n",
                "    plt.imshow(img)\n",
                "    plt.title(f\"Sample Face Image from {os.path.dirname(img_path)}\")\n",
                "    plt.axis(\"off\")\n",
                "    plt.show()\n",
                "else:\n",
                "    print(f\"Image not found at {img_path}. Please update the img_path.\")"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Visualize activation maps\n",
                "if os.path.exists(img_path):\n",
                "    predicted_class = visualizer.visualize_activation_maps(img_path)\n",
                "    print(f\"Predicted emotion: {visualizer.emotion_labels[predicted_class]}\")"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Visualize class activation map\n",
                "if os.path.exists(img_path):\n",
                "    predicted_class, overlay = visualizer.visualize_class_activation_map(img_path)\n",
                "    print(f\"Predicted emotion: {visualizer.emotion_labels[predicted_class]}\")"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

# Save the notebook
with open('activation_maps_demo.ipynb', 'w') as f:
    json.dump(notebook, f, indent=1)

print("Notebook created successfully!") 