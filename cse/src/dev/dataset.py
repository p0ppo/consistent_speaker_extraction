import soundfile as sf
from datasets import load_dataset

ds = load_dataset("diarizers-community/ami", "ihm")
print(ds)

for d in ds["train"]:
    sf.write("sample.wav", d["audio"]["array"], 16000)
    import pdb; pdb.set_trace()