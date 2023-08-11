class HashTable:
	def __init__(self, size):
		self.size = size
		self.hash_table = self.create_buckets()


	def create_buckets(self):
		return [[] for _ in range(self.size)]


	def set_val(self, key, val):
		hashed_key = hash(key) % self.size
		bucket = self.hash_table[hashed_key]
		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			if record_key == key:
				found_key = True
				break
		if found_key:
			bucket[index] = (key, val)
		else:
			bucket.append((key, val))


	def get_val(self, key):
		hashed_key = hash(key) % self.size
		bucket = self.hash_table[hashed_key]
		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			if record_key == key:
				found_key = True
				break
		if found_key:
			return record_val
		else:
			return "Tidak ada di dalam list"


	def delete_val(self, key):
		hashed_key = hash(key) % self.size
		bucket = self.hash_table[hashed_key]
		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			if record_key == key:
				found_key = True
				break
		if found_key:
			bucket.pop(index)
		return
	def __str__(self):
		return "".join(str(item) for item in self.hash_table)
		
hash_table = HashTable(True)


# ============================================================================================================================= #


print()
print("List Value Pada List")
hash_table.set_val('Midu', 'Hai')
print(hash_table)
hash_table.set_val('Mido', 'hai')
print(hash_table)
hash_table.set_val('yoo', 'ada')
print(hash_table)
print()


print("Pencarian Data Pada list :")
print(hash_table.get_val('Midu'))
print()


print("Penghapusan List :")
hash_table.delete_val('Mido')
print(hash_table)
hash_table.delete_val('yoo')
print(hash_table)