from tqdm import tqdm
loop = tqdm(total=10000,position=0,leave=False)
for k in range(50):
    loop.set_description("LOADING....",format(k))
    loop.update(1)
loop.close()
