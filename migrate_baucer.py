import psycopg2
import datetime
import time
import json
from os import system
import keyboard

# time now
timenow = datetime.datetime.now()

# connect db 2
con2 = psycopg2.connect(
	host = "localhost",
	database = "temp_ssipr",
	user = "admin",
	password = "$admin$",
	)


cur2 = con2.cursor()

# -----------------------------------------------------------------------
# CONFIGURATION
# start id with number, cth agensi_id_seq
# report_name = 'report_role.txt'
# column_name = 'role_user'
# start_id_with = 1
# -------------------------------------------------------------------------

with open('data_peserta.json', 'r') as f:
	data = f.read()
	data = data.replace('},]', '}]')

out = json.loads(data)

# total data input
total_data = len(out)
total = 0


# -------------------------------------------------------------------------

# ---------------------------------------------------------------------------

for r in range(len(out)):
# for r in rows:

	# SEND
	if (out[r]["nama"] is not None):

		#cleaning
		if out[r]["tkh_kemaskini"] == '':
			out[r]["tkh_kemaskini"] = str(timenow)

		if out[r]["tkh_dimasukkan"] == '':
			out[r]["tkh_dimasukkan"] = str(timenow)

		if out[r]["kaum"] is not '':

			if out[r]["kaum"] is 'MELAYU':
				out[r]["kaum"] = 'HARI RAYA AIDILFITRI'

			if out[r]["kaum"] is 'CINA':
				out[r]["kaum"] = 'TAHUN BARU CINA'

			if out[r]["kaum"] is 'INDIA':
				out[r]["kaum"] = 'DEEPAVALI'

		# a[4]+a[5] for dun
		# print(out[r]["id_kemasukan"])
		if out[r]["id_kemasukan"] != "":
			namadun = out[r]["id_kemasukan"]

		if out[r]["id_kemasukan"] == 'azizah' and out[r]["dun_pembayar"] == '':
			out[r]["id_kemasukan"] = "2" #sabak

		if out[r]["id_kemasukan"] == 'syanida' and out[r]["dun_pembayar"] == '':
			out[r]["id_kemasukan"] = "31"

		if out[r]["id_kemasukan"] == 'hidayah' and out[r]["dun_pembayar"] == '':
			out[r]["id_kemasukan"] = "14"

		# if out[r]["id_kemasukan"] == 'adun13b' and out[r]["dun_pembayar"] == '':
		# 	out[r]["id_kemasukan"] = "13"

		if out[r]["id_kemasukan"] == 'jannati' and out[r]["dun_pembayar"] == '':
			out[r]["id_kemasukan"] = "32"

		if out[r]["id_kemasukan"] == 'hadi' and out[r]["dun_pembayar"] == '':
			out[r]["id_kemasukan"] = "44"

		if out[r]["id_kemasukan"] == 'rhysa' and out[r]["dun_pembayar"] == '':
			out[r]["id_kemasukan"] = "10"

		if out[r]["id_kemasukan"] == 'sofia' and out[r]["dun_pembayar"] == '':
			out[r]["id_kemasukan"] = "35"

		if out[r]["id_kemasukan"] == 'upen5' and out[r]["dun_pembayar"] == '':
			out[r]["id_kemasukan"] = "8"

		if out[r]["id_kemasukan"] == 'izzul' and out[r]["dun_pembayar"] == '':
			out[r]["id_kemasukan"] = "17"

		if out[r]["id_kemasukan"] == 'azreen' and out[r]["dun_pembayar"] == '':
			out[r]["id_kemasukan"] = "33"

		if out[r]["id_kemasukan"] == 'izan' and out[r]["dun_pembayar"] == '':
			out[r]["id_kemasukan"] = "44"

		if out[r]["id_kemasukan"] == 'upen4' and out[r]["dun_pembayar"] == '':
			out[r]["id_kemasukan"] = "6"

		if out[r]["id_kemasukan"] == 'upen3' and out[r]["dun_pembayar"] == '':
			out[r]["id_kemasukan"] = "27"

		if out[r]["id_kemasukan"] == 'upen6' and out[r]["dun_pembayar"] == '':
			out[r]["id_kemasukan"] = "20"

		# if out[r]["id_kemasukan"] == 'adun9c' and out[r]["dun_pembayar"] == '':
		# 	out[r]["id_kemasukan"] = "9"

		if (len(namadun) >= 4):
			if (namadun[0]+namadun[1]+namadun[2]+namadun[3]) == 'adun' or (namadun[0]+namadun[1]+namadun[2]+namadun[3]) == 'Adun':
				try:
					cek = int(namadun[4])+int(namadun[5])
					out[r]["id_kemasukan"] = namadun[4]+namadun[5]
				except:
					out[r]["id_kemasukan"] = namadun[4]


		if out[r]["id_kemasukan"] != '' and out[r]["dun_pembayar"] != '':
			if out[r]["dun_pembayar"] == "SUNGAI AIR TAWAR":
				out[r]["id_kemasukan"] = "1"
			elif out[r]["dun_pembayar"] == "SABAK":
				out[r]["id_kemasukan"] = "2"
			elif out[r]["dun_pembayar"] == "SUNGAI PANJANG":
				out[r]["id_kemasukan"] = "3"
			elif out[r]["dun_pembayar"] == "SEKINCHAN":
				out[r]["id_kemasukan"] = "4"
			elif out[r]["dun_pembayar"] == "HULU BERNAM":
				out[r]["id_kemasukan"] = "5"
			elif out[r]["dun_pembayar"] == "KUALA KUBU BAHARU":
				out[r]["id_kemasukan"] = "6"
			elif out[r]["dun_pembayar"] == "BATANG KALI":
				out[r]["id_kemasukan"] = "7"
			elif out[r]["dun_pembayar"] == "SUNGAI BURONG":
				out[r]["id_kemasukan"] = "8"
			elif out[r]["dun_pembayar"] == "PERMATANG":
				out[r]["id_kemasukan"] = "9"
			elif out[r]["dun_pembayar"] == "BUKIT MELAWATI":
				out[r]["id_kemasukan"] = "10"
			elif out[r]["dun_pembayar"] == "IJOK":
				out[r]["id_kemasukan"] = "11"
			elif out[r]["dun_pembayar"] == "JERAM":
				out[r]["id_kemasukan"] = "12"
			elif out[r]["dun_pembayar"] == "KUANG":
				out[r]["id_kemasukan"] = "13"
			elif out[r]["dun_pembayar"] == "RAWANG":
				out[r]["id_kemasukan"] = "14"
			elif out[r]["dun_pembayar"] == "TAMAN TEMPLER":
				out[r]["id_kemasukan"] = "15"
			elif out[r]["dun_pembayar"] == "SUNGAI TUA":
				out[r]["id_kemasukan"] = "16"
			elif out[r]["dun_pembayar"] == "GOMBAK SETIA":
				out[r]["id_kemasukan"] = "17"
			elif out[r]["dun_pembayar"] == "HULU KELANG":
				out[r]["id_kemasukan"] = "18"
			elif out[r]["dun_pembayar"] == "BUKIT ANTARABANGSA":
				out[r]["id_kemasukan"] = "19"
			elif out[r]["dun_pembayar"] == "LEMBAH JAYA":
				out[r]["id_kemasukan"] = "20"
			elif out[r]["dun_pembayar"] == "PANDAN INDAH":
				out[r]["id_kemasukan"] = "21"
			elif out[r]["dun_pembayar"] == "TERATAI":
				out[r]["id_kemasukan"] = "22"
			elif out[r]["dun_pembayar"] == "DUSUN TUA":
				out[r]["id_kemasukan"] = "23"
			elif out[r]["dun_pembayar"] == "SEMENYIH":
				out[r]["id_kemasukan"] = "24"
			elif out[r]["dun_pembayar"] == "KAJANG":
				out[r]["id_kemasukan"] = "25"
			elif out[r]["dun_pembayar"] == "SUNGAI RAMAL":
				out[r]["id_kemasukan"] = "26"
			elif out[r]["dun_pembayar"] == "BALAKONG":
				out[r]["id_kemasukan"] = "27"
			elif out[r]["dun_pembayar"] == "SERI KEMBANGAN":
				out[r]["id_kemasukan"] = "28"
			elif out[r]["dun_pembayar"] == "SERI SERDANG":
				out[r]["id_kemasukan"] = "29"
			elif out[r]["dun_pembayar"] == "KINRARA":
				out[r]["id_kemasukan"] = "30"
			elif out[r]["dun_pembayar"] == "SUBANG JAYA":
				out[r]["id_kemasukan"] = "31"
			elif out[r]["dun_pembayar"] == "SERI SETIA":
				out[r]["id_kemasukan"] = "32"
			elif out[r]["dun_pembayar"] == "TAMAN MEDAN":
				out[r]["id_kemasukan"] = "33"
			elif out[r]["dun_pembayar"] == "BUKIT GASING":
				out[r]["id_kemasukan"] = "34"
			elif out[r]["dun_pembayar"] == "KAMPUNG TUNKU":
				out[r]["id_kemasukan"] = "35"
			elif out[r]["dun_pembayar"] == "BANDAR UTAMA":
				out[r]["id_kemasukan"] = "36"
			elif out[r]["dun_pembayar"] == "BUKIT LANJAN":
				out[r]["id_kemasukan"] = "37"
			elif out[r]["dun_pembayar"] == "PAYA JARAS":
				out[r]["id_kemasukan"] = "38"
			elif out[r]["dun_pembayar"] == "KOTA DAMANSARA":
				out[r]["id_kemasukan"] = "39"
			elif out[r]["dun_pembayar"] == "KOTA ANGGERIK":
				out[r]["id_kemasukan"] = "40"
			elif out[r]["dun_pembayar"] == "BATU TIGA":
				out[r]["id_kemasukan"] = "41"
			elif out[r]["dun_pembayar"] == "MERU":
				out[r]["id_kemasukan"] = "42"
			elif out[r]["dun_pembayar"] == "SEMENTA":
				out[r]["id_kemasukan"] = "43"
			elif out[r]["dun_pembayar"] == "SELAT KLANG":
				out[r]["id_kemasukan"] = "44"
			elif out[r]["dun_pembayar"] == "BANDAR BARU KLANG":
				out[r]["id_kemasukan"] = "45"
			elif out[r]["dun_pembayar"] == "PELABUHAN KLANG":
				out[r]["id_kemasukan"] = "46"
			elif out[r]["dun_pembayar"] == "PANDAMARAN":
				out[r]["id_kemasukan"] = "47"
			elif out[r]["dun_pembayar"] == "SENTOSA":
				out[r]["id_kemasukan"] = "48"
			elif out[r]["dun_pembayar"] == "SUNGAI KANDIS":
				out[r]["id_kemasukan"] = "49"
			elif out[r]["dun_pembayar"] == "KOTA KEMUNING":
				out[r]["id_kemasukan"] = "50"
			elif out[r]["dun_pembayar"] == "SIJANGKANG":
				out[r]["id_kemasukan"] = "51"
			elif out[r]["dun_pembayar"] == "BANTING":
				out[r]["id_kemasukan"] = "52"
			elif out[r]["dun_pembayar"] == "MORIB":
				out[r]["id_kemasukan"] = "53"
			elif out[r]["dun_pembayar"] == "TANJUNG SEPAT":
				out[r]["id_kemasukan"] = "54"
			elif out[r]["dun_pembayar"] == "DENGKIL":
				out[r]["id_kemasukan"] = "55"
			elif out[r]["dun_pembayar"] == "SUNGAI PELEK":
				out[r]["id_kemasukan"] = "56"

			# elif out[r]["id_kemasukan"] != 'ana':
			# 	id_kemasukan_tmp = out[r]["id_kemasukan"]
			# 	id_kemasukan_tmp = id_kemasukan_tmp[4]+id_kemasukan_tmp[5]
			# 	out[r]["id_kemasukan"] = int(id_kemasukan_tmp)
			


		# try:
		cur2.execute(
						"""INSERT INTO permohonan_baucer (
						program_id, 
						nama, 
						ic_pemohon, 
						umur, 
						jantina, 
						kaum, 
						no_telefon, 
						pendapatan, 
						nama_pasangan, 
						ic_pasangan, 
						umur_pasangan, 
						pendapatan_pasangan, 
						alamat,
						pendapatan_isi_rumah,
						jumlah_terima,
						perayaan,
						no_tag,
						no_baucer,
						tarikh_terima,
						status_peserta,
						status,
						status_audit,
						tarikh_permohonan,
						dun_pembayar,
						alasan,
						dun_undi,
						dun,
						ipr_id,
						created_at, 
						updated_at
						) 
						VALUES 
						(%s, %s, %s, %s, %s, 
						%s, %s, %s, %s, %s, 
						%s, %s, %s, %s, %s, 
						%s, %s, %s, %s, %s, 
						%s, %s, %s, %s, %s, 
						%s, %s, %s, %s, %s)""", 
						(
							out[r]["id_program"], 
							out[r]["nama"], 
							out[r]["no_kp"], 
							out[r]["umur_peserta"], 
							out[r]["jantina"], 
							out[r]["kaum"], 
							out[r]["no_telefon"], 
							out[r]["pendapatan_peserta"], 
							out[r]["nama_pasangan"], 
							out[r]["nokp_pasangan"], 
							out[r]["umur_pasangan"], 
							out[r]["pendapatan_pasangan"], 
							out[r]["alamat"],
							out[r]["semua_pendapatan"],
							out[r]["jumlah_diterima"],
							out[r]["kaum"],
							out[r]["no_tag"],
							out[r]["no_baucer"],
							out[r]["tkh_dimasukkan"],
							out[r]["status"],
							2,
							1,
							out[r]["tkh_dimasukkan"],
							out[r]["dun_pembayar"],
							out[r]["catatan"],
							out[r]["undi_dun"],
							out[r]["id_kemasukan"],
							14,
							out[r]["tkh_dimasukkan"],
							out[r]["tkh_kemaskini"],
						)
					)
		# print(out[r]["no_kp"] + " = OK", )
		total = total+1

		if keyboard.is_pressed('s'):
			print('exiting..')
			# close
			cur2.close()
			con2.close()
			exit()

		# Print status every 1000 addresses
		if total % 10000 == 0:
			print("Completed {} of {} data".format( total, len(out) ))

		# percent = float((total/total_data)*100)
		# print(str(round(percent, 3))+' %')
		# system('clear')



		# write report
		# with open(report_name, 'a') as the_file:
		# 	the_file.write(f"{r[3]} = OK\n")
		# except:
			# print("except ERROR")


	else:
		# print(f"{out[r]["no_kp"]} = ERROR\n")
		# print(out[r]["no_kp"])
		# total_error += 1
		print("ERROR")

		# write report
		# with open(report_name, 'a') as the_file:
		# 	the_file.write(f"{r[0]} = ERROR\n")

	# time.sleep(0.01)


# ---------------------------------------------------------------------------

cur2.execute("SELECT * FROM permohonan_baucer")

# save data to db
# con2.commit()

# fetch all
rows2 = cur2.fetchall()

# output
# for r in rows2:
# 	print (r)
# 	print ('\n')
	# print (r[0])

# show done_migrate
# print(done_migrate)
# print('\n')

# # show total ERROR
# print(f'\nTotal ERROR = {total_error}\n')
# print(f'Total SKIP = {total_skip}\n')
# # write report
# with open(report_name, 'a') as the_file:
# 	the_file.write(f'\nTotal ERROR = {total_error}\n')
# 	the_file.write(f'Total SKIP = {total_skip}\n')
print("TOTAL DATA = " + str(total_data))
print("TOTAL DATA MIGRATE = " + str(total))

# close cursor
cur2.close()

# close connection
con2.close()