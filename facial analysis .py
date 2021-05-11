import boto3
import cv2
import IPython

cap = cv2.VideoCapture(0)
while True:
    myphoto = "mypic.jpg"
    ret, photo = cap.read()
    cv2.imshow(myphoto,photo)
    cv2.imwrite(myphoto, photo)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

region = "ap-south-1"
bucket = "miniprojecttyit"

uploaded_image = "pic.jpg"

s3 = boto3.resource('s3')
s3.Bucket(bucket).upload_file(myphoto, uploaded_image)
rek = boto3.client('rekognition', region)

responce = rek.detect_faces(Image={
        "S3Object": {
            "Bucket": bucket,
            "Name": uploaded_image
        }}, Attributes = ['ALL'])

def play_song(song_name):
    from pygame import mixer
    mixer.init()
    mixer.music.load(song_name)
    mixer.music.set_volume(0.7)
    mixer.music.play()
    while True:
        print("p to pause\nr to resume\ne to exit\n")
        query = input(" ")
        if query == 'p':
            mixer.music.pause()	
        elif query == 'r':
            mixer.music.unpause()
        elif query == 'e':
            mixer.music.stop()
            break

while True:
    if responce['FaceDetails'][0]['Emotions'][0]['Type'] == 'CALM' and responce['FaceDetails'][0]['Emotions'][0]['Confidence'] >= 50:
            print("1.Dil Diyan Gallan.mp3\n2.Kal-Ho-Na-Ho.mp3\n3.Maahi Ve.mp3\n")
            ch = input("Which song would you like to play : ")
            if ch == '1':
                print("Playing Song")
                play_song("songs/Calm/Dil Diyan Gallan (Tiger Zinda Hai) 128 Kbps.mp3")
            elif ch == '2':
                print("Playing Song")
                play_song("songs/Calm/Kal-Ho-Na-Ho-Instrumental-(pagalworldsongs.co.in).mp3")
            elif ch == '3':
                print("Playing Song")
                play_song("songs/Calm/Maahi Ve (Wajah Tum Ho) 128 Kbps.mp3")
            else:
                break

    elif responce['FaceDetails'][0]['Emotions'][0]['Type'] == 'HAPPY' and responce['FaceDetails'][0]['Emotions'][0]['Confidence'] >= 50:
            print("1.Chittiyaan-Kalaiyaan.mp3\n2.Roobaroo.mp3\n3.senorita.mp3\n")
            ch = input("Which song would you like to play : ")
            if ch == '1':
                print("Playing Song")
                play_song("songs/Happy/Chittiyaan-Kalaiyaan-b-Roy-(pagalworldsongs.co.in).mp3")
            elif ch == '2':
                print("Playing Song")
                play_song("songs/Happy/Roobaroo-(pagalworldsongs.co.in).mp3")
            elif ch == '3':
                print("Playing Song")
                play_song("songs/Happy/senorita.mp3")
            else:
                break

    elif responce['FaceDetails'][0]['Emotions'][0]['Type'] == 'SURPRISED' and responce['FaceDetails'][0]['Emotions'][0]['Confidence'] >= 50:
            print("1.Hai Junoon.mp3\n2.Aaj Main Upar.mp3\n3.Ilahi.mp3\n4.Life-Is-Crazy.mp3\n")
            ch = input("Which song would you like to play : ")
            if ch == '1':
                print("Playing Song")
                play_song("songs/Surprised/01. Hai Junoon.mp3")
            elif ch == '2':
                print("Playing Song")
                play_song("songs/Surprised/Aaj Main Upar - (amlijatt.in).mp3")
            elif ch == '3':
                print("Playing Song")
                play_song("songs/Surprised/Ilahi-(pagalworldsongs.co.in).mp3")
            elif ch == '4':
                print("Playing Song")
                play_song("songs/Surprised/Life-Is-Crazy-(pagalworldsongs.co.in).mp3")
            else:
                break

    elif responce['FaceDetails'][0]['Emotions'][0]['Type'] == 'DISGUSTED' and responce['FaceDetails'][0]['Emotions'][0]['Confidence'] >= 50:
            print("1.Agar Tum Saath Ho.mp3\n2.Kabira.mp3\n3.Maana Ke Hum Yaar Nahi.mp3\n")
            ch = input("Which song would you like to play : ")
            if ch == '1':
                print("Playing Song")
                play_song("songs/Disgust/Agar Tum Saath Ho(PaglaSongs).mp3")
            elif ch == '2':
                print("Playing Song")
                play_song("songs/Disgust/Kabira.mp3")
            elif ch == '3':
                print("Playing Song")
                play_song("songs/Disgust/Maana Ke Hum Yaar Nahi (Meri Pyaari Bindu) 128 Kbps.mp3")
            else:
                break

    elif responce['FaceDetails'][0]['Emotions'][0]['Type'] == 'CONFUSED' and responce['FaceDetails'][0]['Emotions'][0]['Confidence'] >= 50:
            print("1. Kuch-To-Hua-Hai.mp3\n2.Tum-Ho.mp3\n3.Zara-Sa-Power-Ballad.mp3\n")
            ch = input("Which song would you like to play : ")
            if ch == '1':
                print("Playing Song")
                play_song("songs/confused/Kuch-To-Hua-Hai-(pagalworldsongs.co.in).mp3")
            elif ch == '2':
                print("Playing Song")
                play_song("songs/confused/Tum-Ho-(pagalworldsongs.co.in).mp3")
            elif ch == '3':
                print("Playing Song")
                play_song("songs/confused/Zara-Sa-Power-Ballad-(pagalworldsongs.co.in).mp3")
            else:
                break

    elif responce['FaceDetails'][0]['Emotions'][0]['Type'] == 'FEAR' and responce['FaceDetails'][0]['Emotions'][0]['Confidence'] >= 50:
            print("1.breathin.mp3\n2.In My Blood.mp3\n")
            ch = input("Which song would you like to play : ")
            if ch == '1':
                print("Playing Song")
                play_song("songs/fear/Ariana Grande - breathin (Official Video) (320  kbps).mp3")
            elif ch == '2':
                print("Playing Song")
                play_song("songs/fear/Shawn Mendes - In My Blood.mp3")
            else:
                break
                
    elif responce['FaceDetails'][0]['Emotions'][0]['Type'] == 'ANGRY' and responce['FaceDetails'][0]['Emotions'][0]['Confidence'] >= 50:
            print("Playing Song")
            play_song("happy.mp3") 

    elif responce['FaceDetails'][0]['Emotions'][0]['Type'] == 'SAD' and responce['FaceDetails'][0]['Emotions'][0]['Confidence'] >= 50:
            print("1.Abhi Mujh Mein Kahin.mp3\n2.Bekhayali.mp3\n3.Baarish.mp3\n4.adap-Tadap-Ke.mp3\n")
            ch = input("Which song would you like to play : ")
            if ch == '1':
                print("Playing Song")
                play_song("songs/Sad/Abhi Mujh Mein Kahin.mp3")
            elif ch == '2':
                print("Playing Song")
                play_song("songs/Sad/Bekhayali - Kabir Singh 128 Kbps.mp3")
            elif ch == '3':
                print("Playing Song")
                play_song("songs/Sad/Baarish (Half Girlfriend) 128 Kbps.mp3")
            elif ch == '4':
                print("Playing Song")
                play_song("songs/Sad/Tadap-Tadap-Ke-(pagalworldsongs.co.in).mp3")
            else:
                break
    else:
        x = input("Please specify any song:")
        if (("romantic" in x) or ("romance" in x)):
            print("1.Ishq Ki Baarish.mp3\n2.Ishq-Wala-Love.mp3\n3.Muskurane.mp3")
            ch = input("Which song would you like to play : ")
            if ch == '1':
                print("Playing Song")
                play_song("songs/Romantic/05 Ishq Ki Baarish (DjBewafa.Com).mp3")
            elif ch == '2':
                print("Playing Song")
                play_song("songs/Romantic/Ishq-Wala-Love-(pagalworldsongs.co.in).mp3")
            elif ch == '3':
                print("Playing Song")
                play_song("songs/Romantic/Muskurane-(Unplugged)-(pagalworldsongs.co.in).mp3")
            else:
                break

