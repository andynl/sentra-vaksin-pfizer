import requests

def main():
    headers = {
            'Authorization': 'Bearer 2|1mcB0aYZjD4manNttOKyt5nE3PquT96yIDQYxofq', 
            'Host': 'vaksinasi-corona.jakarta.go.id', 
            'Referer': 'https://vaksinasi-corona.jakarta.go.id', 
            'Origin': 'https://vaksinasi-corona.jakarta.go.id'
        }
    
    faskes = [
        {'faskes' : 'GEDUNG JUDO KELAPA GADING', 'kota': 'KOTA ADM. JAKARTA UTARA', 'kecamatan': 'KELAPA GADING', 'kelurahan': 'KELAPA GADING TIMUR'},
        {'faskes' : 'GOR PENGADEGAN-PFIZER', 'kota': 'KOTA ADM. JAKARTA SELATAN', 'kecamatan': 'PANCORAN', 'kelurahan': 'PENGADEGAN'},
        {'faskes' : 'MAL KOTA KASABLANKA - PFIZER', 'kota': 'KOTA ADM. JAKARTA SELATAN', 'kecamatan': 'TEBET', 'kelurahan': 'MENTENG DALAM'},
        {'faskes' : 'PUSKESMAS KECAMATAN JOHAR BARU', 'kota': 'KOTA ADM. JAKARTA PUSAT', 'kecamatan': 'JOHAR BARU', 'kelurahan': 'JOHAR BARU'},
        {'faskes' : 'PUSKESMAS KECAMATAN CILANDAK', 'kota': 'KOTA ADM. JAKARTA SELATAN', 'kecamatan': 'CILANDAK', 'kelurahan': 'CILANDAK BARAT'},
        {'faskes' : 'PUSKESMAS KELURAHAN LEBAK BULUS', 'kota': 'KOTA ADM. JAKARTA SELATAN', 'kecamatan': 'LEBAK BULUS', 'kelurahan': 'LEBAK BULUS'},
        {'faskes' : 'PUSKESMAS KELURAHAN PANCORAN', 'kota': 'KOTA ADM. JAKARTA SELATAN', 'kecamatan': 'PANCORAN', 'kelurahan': 'PANCORAN'},
        {'faskes' : 'RS PRIKASIH', 'kota': 'KOTA ADM. JAKARTA SELATAN', 'kecamatan': 'CILANDAK', 'kelurahan': 'PONDOK LABU'},
        {'faskes' : 'RS TK. IV KESDAM CIJANTUNG', 'kota': 'KOTA ADM. JAKARTA TIMUR', 'kecamatan': 'PASAR REBO', 'kelurahan': 'GEDONG'},
        {'faskes' : 'RSIA FAMILY', 'kota': 'KOTA ADM. JAKARTA UTARA', 'kecamatan': 'PENJARINGAN', 'kelurahan': 'PEJAGALAN'},
        {'faskes' : 'RSKD DUREN SAWIT', 'kota': 'KOTA ADM. JAKARTA TIMUR', 'kecamatan': 'DUREN SAWIT', 'kelurahan': 'DUREN SAWIT'},
        {'faskes' : 'RSUD TUGU KOJA', 'kota': 'KOTA ADM. JAKARTA UTARA', 'kecamatan': 'KOJA', 'kelurahan': 'TUGU UTARA'},
        {'faskes' : 'SENTRA VAKSINASI PFIZER WALIKOTA JAKSEL', 'kota': 'KOTA ADM. JAKARTA SELATAN', 'kecamatan': 'KEBAYORAN BARU', 'kelurahan': 'PETOGOGAN'},
        {'faskes' : 'SMKN 26 JAKARTA', 'kota': 'KOTA ADM. JAKARTA TIMUR', 'kecamatan': 'PULOGADUNG', 'kelurahan': 'PULOGADUNG'},
        {'faskes' : 'SMPN 86 JAKARTA-PFIZER', 'kota': 'KOTA ADM. JAKARTA SELATAN', 'kecamatan': 'CILANDAK', 'kelurahan': 'CILANDAK BARAT'},
        {'faskes' : 'RSUD JATIPADANG', 'kota': 'KOTA ADM. JAKARTA SELATAN', 'kecamatan': 'PASAR MINGGU', 'kelurahan': 'JATI PADANG'},

    ]

    payloads = []
    for sentra in faskes:    
        pld  = {
            'nik': '-',
            'nama': '-',
            'pcare': 'true',
            'wilayah': sentra['kota'],
            'kecamatan': sentra['kecamatan'],
            'kelurahan': sentra['kelurahan'],
            'type_vaksin': 'first',
        }
        payloads.append(pld)

    for payload in payloads:
        r = requests.get("https://vaksinasi-corona.jakarta.go.id/service/api/faskes", params=payload, headers=headers)
        data = r.json()
        if len(data) > 0:
            for sentra in data:
                print('ADA KUOTA VAKSIN PFIZER DI {nama}'.format(nama=sentra['nama_lokasi_vaksinasi']))
        else:
            print('GAK ADA KUOTA VAKSIN PFIZER DI {nama}'.format(nama=payload['kelurahan']))

if __name__ == "__main__":
    main()