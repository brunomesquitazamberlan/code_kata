import time
from concurrent.futures import ThreadPoolExecutor


def fetch_profile(user_id: int) -> dict:
    time.sleep(0.2)

    return {"id": user_id, "name": f"User {user_id}"}


def fetch_profiles_sequential(user_ids: list[int]) -> list[dict]:
    return [fetch_profile(user_id) for user_id in user_ids]


def fetch_profiles_concurrent(user_ids: list[int], n_workers: int) -> list[dict]:
    with ThreadPoolExecutor(max_workers=n_workers) as thread_pool:
        return list(thread_pool.map(fetch_profile, user_ids))


if __name__ == "__main__":
    user_ids = [1, 2, 3, 4, 5]

    start_seq = time.perf_counter()
    fetch_profiles_sequential(user_ids)
    end_seq = time.perf_counter()
    print(f"Sequential needs {end_seq - start_seq} seconds")

    start_conc = time.perf_counter()
    fetch_profiles_concurrent(user_ids, 10)
    end_conc = time.perf_counter()
    print(f"Concurrent needs {end_conc - start_conc} seconds")
