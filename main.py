
from music_logger import generate_log
from song_sorter import sort_songs


def merge_folders(main_folder_path, source_folder_path):
    main_log = generate_log(main_folder_path)
    source_log = generate_log(source_folder_path)
    
main_folder_path = r"D:\Equipo\Documentos\Base de Datos\Trabajo\Proyectos Secundarios\2024 Music_Sorter\test\Music_Destination"
source_folder_path = r"D:\Equipo\Documentos\Base de Datos\Trabajo\Proyectos Secundarios\2024 Music_Sorter\test\Music_Origin"
sort_songs(main_folder_path)