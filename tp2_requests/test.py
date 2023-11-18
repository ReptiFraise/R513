# %% [markdown]
# Import requests

# %%
import requests

# %% [markdown]
# Accès à la route / de 127.0.0.1:5000 et affiche le message de bienvenue

# %%
r = requests.get("https://localhost:5001", verify="web/cert.pem")
print(r.text.split("<h1>")[1].split("</h1>")[0])

# %% [markdown]
# Accès à la route /private avec login bob:sponge en basique et affiche le message de la page

# %%
r = requests.get("https://localhost:5001/private", auth=("bob","sponge"), verify="web/cert.pem")
print(r.text.split("<h1>")[1].split("</h1>")[0])

# %% [markdown]
# Accès à la route /upload et téléverse le fichier

# %%
with open("/home/admin/wget.txt", "rb") as file:
    r = requests.post(f"https://localhost:5001/upload", files={"file": file}, verify="web/cert.pem")
    print(r.status_code)


