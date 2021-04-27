users = ['mike', 'sam', 'baz', 'york', 'ant']
banned_users =['tom', 'lewis', 'harry']

if banned_users not in users:
    print(f"Sorry {banned_users}, you are still banned.")
else:
    print(f"\nGood job {users}, you are still active")



