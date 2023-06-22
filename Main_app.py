class Node:
  def __init__(self, sku, nama_barang, harga_satuan, jumlah_stok):
    self.sku = sku
    self.nama_barang = nama_barang
    self.harga_satuan = harga_satuan
    self.jumlah_stok = jumlah_stok
    self.left = None
    self.right = None


class BinarySearchTree:
  def __init__(self):
    self.root = None

  def is_empty(self):
    return self.root is None

  def insert_barang(self, sku, nama_barang, harga_satuan, jumlah_stok):
    if self.is_empty():
      self.root = Node(sku, nama_barang, harga_satuan, jumlah_stok)
    else:
      current = self.root
      while True:
        if sku == current.sku:
          print("No. SKU sudah tersimpan di dalam BST.")
          return
        elif sku < current.sku:
          if current.left is None:
            current.left = Node(sku, nama_barang, harga_satuan, jumlah_stok)
            break
          else:
            current = current.left
        else:
          if current.right is None:
            current.right = Node(sku, nama_barang, harga_satuan, jumlah_stok)
            break
          else:
            current = current.right
      print("Data stok barang berhasil disimpan.")

  def restock(self, sku, restock_amount):
    current = self.root
    while current:
      if sku == current.sku:
        current.jumlah_stok += restock_amount
        print("Restok barang berhasil dilakukan.")
        return
      elif sku < current.sku:
        current = current.left
      else:
        current = current.right
    print("No. SKU belum tersimpan di dalam BST")
    print("Silakan input data stok barang terlebih dahulu.")

  def search(self, sku):
    current = self.root
    while current is not None:
      if sku == current.sku:
        return current
      elif sku < current.sku:
        current = current.left
      else:
        current = current.right
    return None


class Transaksi:
  def __init__(self, nama_pelanggan, sku, quantity):
    self.nama_pelanggan = nama_pelanggan
    self.sku = sku
    self.quantity = quantity

  def hitung_subtotal(self, bst):
    node = bst.search(self.sku)
    if node is not None:
      subtotal = node.harga_satuan * self.quantity
      return subtotal
    else:
      return None


def input_data_stok():
  sku = input("Masukkan No. SKU (4 digit angka): ")
  nama_barang = input("Masukkan Nama Barang: ")
  harga_satuan = float(input("Masukkan Harga Satuan: "))
  jumlah_stok = int(input("Masukkan Jumlah Stok: "))
  return sku, nama_barang, harga_satuan, jumlah_stok


def input_restock():
  sku = input("Masukkan No. SKU barang yang akan direstok: ")
  restock_amount = int(input("Masukkan jumlah stok baru yang akan ditambahkan: "))
  return sku, restock_amount


def display_inputData_dan_restok():
  while True:
    print("\n=== MENU KELOLA STOK BARANG ===")
    print("1. Input Data Stok Barang")
    print("2. Restok Barang")
    print("0. Kembali ke MENU UTAMA")

    pilihan = int(input("Pilih menu: "))

    if pilihan == 1:
      sku, nama_barang, harga_satuan, jumlah_stok = input_data_stok()
      bst.insert_barang(sku, nama_barang, harga_satuan, jumlah_stok)
    elif pilihan == 2:
      sku, restock_amount = input_restock()
      bst.restock(sku, restock_amount)
    elif pilihan == 0:
      menu_utama()
    else:
      print("Pilihan Anda Tidak Ada!!!")


def input_data_transaksi(daftar_transaksi):
  nama_customer = input("Masukkan Nama Konsumen: ")
  sku = input("Masukkan No. SKU barang yang dibeli: ")
  jumlah = int(input("Masukkan Jumlah Beli: "))

  node = bst.search(sku)
  if node:
    if node.jumlah_stok >= jumlah:
      harga = node.harga_satuan
      node.jumlah_stok -= jumlah
      transaction = Transaksi(nama_customer, sku, jumlah)
      daftar_transaksi.append(transaction)
      print("Data transaksi berhasil diinputkan.")
      choice = input("Apakah ingin menambahkan data pembelian untuk konsumen ini (y/n)? ")
      if choice.lower() == 'y':
        input_data_transaksi(daftar_transaksi)
    else:
      print("Jumlah stok No. SKU yang Anda beli tidak mencukupi.")
      choice = input("Apakah ingin melanjutkan transaksi (y/n)? ")
      if choice.lower() == 'y':
        input_data_transaksi(daftar_transaksi)
  else:
    print("No. SKU yang diinputkan belum terdaftar.")
    choice = input("Apakah ingin melanjutkan transaksi (y/n)? ")
    if choice.lower() == 'y':
      input_data_transaksi(daftar_transaksi)


def display_transaksi(daftar_transaksi):
  print("Data Seluruh Transaksi Konsumen:")
  print("Nama Konsumen | No. SKU | Jumlah Beli | Subtotal")
  for transaksi in daftar_transaksi:
    subtotal = transaksi.hitung_subtotal(bst)
    print(transaksi.nama_pelanggan,'\t', transaksi.sku,'\t\t', transaksi.quantity,'\t', subtotal)


def sort_transaksi(daftar_transaksi):
  sorted_transaksi = sorted(daftar_transaksi, key=lambda x: x.hitung_subtotal(bst), reverse=True)
  print("Data Transaksi Berdasarkan Subtotal:")
  print("Nama Konsumen | No. SKU | Jumlah Beli | Subtotal")
  for transaksi in sorted_transaksi:
    subtotal = transaksi.hitung_subtotal(bst)
    print(transaksi.nama_pelanggan,'\t', transaksi.sku,'\t\t', transaksi.quantity,'\t', subtotal)


def menu_utama():
  while True:
    print("\n======= MENU UTAMA =========")
    print("1. Kelola Stok Barang")
    print("2. Kelola Transaksi Konsumen")
    print("0. Exit Program")
    print("============================")

    pilihan = int(input("Pilih menu: "))

    if pilihan == 1:
      display_inputData_dan_restok()
    elif pilihan == 2:
      menu_kelola_transaksi()
    elif pilihan == 0:
      exit()
    else:
      print("Pilihan Tidak Ada!!!")


def menu_kelola_transaksi():
  global bst 
  daftar_transaksi = []
  while True:
    print("\n=== MENU KELOLA TRANSAKSI KONSUMEN ===")
    print("1. Input Data Transaksi Baru")
    print("2. Lihat Data Seluruh Transaksi Konsumen")
    print("3. Lihat Data Transaksi Berdasarkan Subtotal")
    print("0. Kembali ke MENU UTAMA")

    pilihan = int(input("Pilih menu: "))

    if pilihan == 1:
      input_data_transaksi(daftar_transaksi)
    elif pilihan == 2:
      display_transaksi(daftar_transaksi)
    elif pilihan == 3:
      sort_transaksi(daftar_transaksi)
    elif pilihan == 0:
      menu_utama()
    else:
      print("Pilihan Anda Tidak Ada!!!")


if __name__ == "__main__":
  bst = BinarySearchTree()
  menu_utama()
