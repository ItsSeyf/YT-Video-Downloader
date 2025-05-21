import yt_dlp

def descargar_video(url):
    opciones = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        try:
            print(f"Descargando {url} en la mejor calidad disponible...")
            ydl.download([url])
            print("Descarga completa!")
        except Exception as e:
            print(f"Error al descargar el video: {e}")


descargar_video(input('Ingrese la URL del video'))