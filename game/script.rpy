# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
#image bg blck = "images/blck.png"
image term = "images/terminal.jpg"
image botan = "images/botan.png"
image kamar = "images/Kamar.jpg"
image balkon = "images/balkon.jpg"
# Deklarasikan karakter yang digunakan di game.
define e = Character('Botan', color="#000000")

# Game dimulai disini.
label start:

'"Kita akan selalu bersama."'
'"Tidak ada yang bisa memisahkan kita.”'
'"Bahkan jika itu adalah kematian sekalipun"'

"Kalimat-kalimat itulah yang selalu ada dalam pikiranku."

scene kamar with fade
play sound "audio/alarm.mp3"
#    scene bg blck with dissolve
"Jam dua malam, alarm berdering dari jam weker tua yang setia melayani diriku semenjak aku berumur 18 tahun."
"Selama tiga tahun melayaniku, baru kali ini deringnya terdengar serak."
"Rasa tak ingin keluar dari selimut yang memelukku dengan erat berhasil dikalahkan oleh suara dering yang menusuk telingaku."
"Terpaksa aku harus mengorbankan tangan kananku keluar dari dalam selimut untuk mematikan jam weker tua sialan itu."
"Setelah 39 detik hanya berbaring menatap langit-langit kamar seluas 4x3 meter" 
"Aku mulai mengangkat rangka dalam tubuhku agar bisa duduk di sisi ranjang."
"Terima kasih kepada selimut yang enggan melepasku ketika tertidur, tubuhku menjadi  berkeringat."
"Aku mulai berdiri melihat ke arah balkon apartemen ini."
scene balkon with fade
"Ibu kota tidak pernah tertidur, "
"bahkan jika seisi kota dibius menggunakan obat tidur dengan dosis paling kuat sekalipun, "
"akan ada pembuluh darah yang akan berusaha menyadarkan Ibu kota. "
"Rasanya aku ingin membasuh badanku dengan air."
"Ketika ingin menggerakakan kakiku ke kamar mandi, aku baru mengingat sesuatu."
"Sayangnya kamar mandi apartemen ini sedang tidak bisa digunakan."
"Aku bahkan ragu akan ada orang yang akan menggunakan kamar mandi itu lagi."
"Setidaknya aku bisa menikmati minuman berkarbonasi dari dalam lemari pendingin." 


return
