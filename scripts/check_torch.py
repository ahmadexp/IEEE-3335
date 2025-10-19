"""Check PyTorch CUDA status."""
import sys

try:
    import torch
    print(f"PyTorch version: {torch.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")
    
    if torch.cuda.is_available():
        print(f"CUDA version: {torch.version.cuda}")
        print(f"GPU: {torch.cuda.get_device_name(0)}")
    else:
        print("\nCUDA is NOT available.")
        if '+cpu' in torch.__version__:
            print("You have the CPU-only version of PyTorch installed.")
        print("\nTo install CUDA version:")
        print("  uv pip install torch --index-url https://download.pytorch.org/whl/cu121")
        
except ImportError:
    print("PyTorch is not installed!")
    print("Install with: uv sync --extra cuda")
