Cloud Run 
Cloud Run adalah platform kokmputasi terkelola yang memungkinkan programmer menjalankan container langsung di infrastruktur skalabel Google.
Cara untuk menjalankan kode:
1. Cloud Run services, digunakan untuk menjalanakan kode yagn merespon web request atau events
2. Cloud Run jobs, digunakan untuk menjalankan kode yang menajalan pekerjaan (job) dan berhenti saat pekerjaan selesai.

Client -> (Web requests and event) -> HTTPS endpoint -> Container instance

Cloud Run service memberi user infrastruktur yang diperlukan untuk menjalankan endpoints HTTPS. Tanggung jawab programmer adalah memastikan kode didengarkan di TCP port dan menangani HTTP requests.

===Tahap membuat cloud run service===

Permissions yang dibutuhakan untuk deploy setidaknya memilki stau dari berikut:
-Owner
-Editor
-Both the Cloud Run Admin and Service Account User roles.
-Cloudrun-Deployer
-Any custom role that includes ithis specific list of permissions

Programmer dapat menggunakan image container, yang disimpan di
-Container Registry atau
-Artifact Registry

catatan :
-Jika telah memberikan roles Artifact Registry apapun di tingkat project, role tersebut akan diwariskan oleh repositori dalam project. JIka ingin anggota tim memiliki tingkat akses yang berbeda ke repositori dalam project, berikan peran di tingkat repositori

Dalam membuat cloud run service disini menggunakan 2 repository:
-Artifact Registry repository : repositori untuk menyimpan images python
-Cloud Source repositories : repositori untuk menyimpan source code python

Kegunaan FIle:
-FIle python main sebagai aplikasi web service user
-File Dockerfile membuat docker container python-image untuk menjalankan aplikasi web service user
-File yaml cloudbuild:
    -build python image
    -push python image ke artifact registry repository
    -deploy cloud run service
-File txt requerements digunakan dockerfile untuk membuat python image dengan library yang dibutuhkan aplikasi user
-File .gitignore untuk file/folder yang tidak ingin di push ke cloud source repositories

Tahap:
    1. Mempersiapkan artifact registry repository untuk menyimpan python image
        1. Mengisi Name artifact regisrty repositorynya,