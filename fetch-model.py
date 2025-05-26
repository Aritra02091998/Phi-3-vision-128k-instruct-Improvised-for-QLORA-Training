from huggingface_hub import snapshot_download

# Downloads everything to a local folder named "phi-3"
snapshot_download(
    repo_id="microsoft/Phi-3-vision-128k-instruct",
    local_dir="Phi-3-vision-128k-instruct",
    local_dir_use_symlinks=False  # Ensures full copies, not symlinks
)
