import subprocess
import os
import argparse
import sys

def download_video(url, output_path=None, format="best", verbose=False):
    """
    Descarga un video de YouTube usando yt-dlp
    
    Args:
        url (str): URL del video
        output_path (str, opcional): Ruta donde guardar el video
        format (str): Formato de descarga (best, bestvideo+bestaudio, etc.)
        verbose (bool): Mostrar salida detallada
    
    Returns:
        bool: True si la descarga fue exitosa, False en caso contrario
    """
    try:
        # Verificar si yt-dlp está instalado
        try:
            subprocess.run(["yt-dlp", "--version"], capture_output=True, check=True)
        except (subprocess.SubprocessError, FileNotFoundError):
            print("yt-dlp no está instalado. Instalando...")
            subprocess.run([sys.executable, "-m", "pip", "install", "yt-dlp"], check=True)
            print("yt-dlp instalado correctamente.")
        
        # Preparar comandos
        cmd = ["yt-dlp"]
        
        # Añadir formato
        if format:
            cmd.extend(["-f", format])
        
        # Configurar ruta de salida
        if output_path:
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            # Usar formato de salida apropiado
            output_template = os.path.join(output_path, "%(title)s.%(ext)s")
            cmd.extend(["-o", output_template])
        
        # Añadir URL
        cmd.append(url)
        
        # Añadir opciones adicionales
        cmd.extend(["--no-warnings"])
        
        if verbose:
            print(f"Ejecutando comando: {' '.join(cmd)}")
        
        # Ejecutar descarga
        print("\nIniciando descarga con yt-dlp...")
        process = subprocess.run(cmd, text=True, capture_output=not verbose)
        
        if process.returncode == 0:
            print("\n¡Descarga completada con éxito!")
            return True
        else:
            print(f"\nError durante la descarga: {process.stderr}")
            return False
            
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        return False

def interactive_mode():
    """Modo interactivo para descargar videos"""
    print("=== Descargador de Videos de YouTube (yt-dlp) ===")
    
    url = input("\nIngresa la URL del video: ")
    
    output_path = input("Ingresa la ruta de descarga (deja en blanco para usar la carpeta actual): ")
    if output_path.strip() == "":
        output_path = None
    
    print("\nSelecciona el formato de descarga:")
    print("1. Mejor calidad general (opción recomendada)")
    print("2. Mejor video + mejor audio (puede requerir post-procesamiento)")
    print("3. Video de 720p")
    print("4. Solo audio (mejor calidad)")
    
    format_choice = input("\nIngresa el número de tu elección (1-4) o presiona Enter para opción 1: ")
    
    formats = {
        "1": "best",
        "2": "bestvideo+bestaudio",
        "3": "bestvideo[height<=720]+bestaudio/best[height<=720]",
        "4": "bestaudio"
    }
    
    format_option = formats.get(format_choice.strip(), "best")
    
    verbose = input("\n¿Mostrar información detallada durante la descarga? (s/n): ").lower().startswith('s')
    
    print("\nComenzando descarga...")
    download_video(url, output_path, format_option, verbose)

def main():
    # Configurar argumentos de línea de comandos para uso no interactivo
    parser = argparse.ArgumentParser(description="Descargador de videos de YouTube usando yt-dlp")
    parser.add_argument("--url", help="URL del video a descargar")
    parser.add_argument("--output", help="Ruta de salida para guardar el video")
    parser.add_argument("--format", default="best", help="Formato de descarga (best, bestvideo+bestaudio, etc.)")
    parser.add_argument("--verbose", action="store_true", help="Mostrar información detallada")
    parser.add_argument("--interactive", action="store_true", help="Usar modo interactivo")
    
    args = parser.parse_args()
    
    # Si se especifica modo interactivo o no hay URL, entrar en modo interactivo
    if args.interactive or not args.url:
        interactive_mode()
    else:
        # Modo no interactivo con argumentos
        download_video(args.url, args.output, args.format, args.verbose)

if __name__ == "__main__":
    main()