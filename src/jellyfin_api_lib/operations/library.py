from jellyfin_api_lib.types import Unset
from result import Err, Ok, Result

from ..api.environment import validate_path
from ..api.library_structure import add_virtual_folder, get_virtual_folders, remove_virtual_folder
from ..models.add_virtual_folder_dto import AddVirtualFolderDto
from ..models.collection_type_options import CollectionTypeOptions
from ..models.library_options import LibraryOptions
from ..models.validate_path_dto import ValidatePathDto
from ..models.virtual_folder_info import VirtualFolderInfo

default_library_options = LibraryOptions(
    enable_photos=True,
    enable_realtime_monitor=True,
    enable_chapter_image_extraction=False,
    extract_chapter_images_during_library_scan=False,
    path_infos=[],
    save_local_metadata=False,
    enable_internet_providers=True,
    enable_automatic_series_grouping=False,
    enable_embedded_titles=False,
    enable_embedded_episode_infos=False,
    automatic_refresh_interval_days=0,
    preferred_metadata_language=None,
    metadata_country_code=None,
    season_zero_display_name="Specials",
    metadata_savers=None,
    disabled_local_metadata_readers=[],
    local_metadata_reader_order=None,
    disabled_subtitle_fetchers=[],
    subtitle_fetcher_order=["Open Subtitles"],
    skip_subtitles_if_embedded_subtitles_present=False,
    skip_subtitles_if_audio_track_matches=False,
    subtitle_download_languages=None,
    require_perfect_subtitle_match=True,
    save_subtitles_with_media=True,
    automatically_add_to_collection=False,
    allow_embedded_subtitles=Unset,
    type_options=Unset,
)


def get_libraries(client) -> Result[list[VirtualFolderInfo], str]:
    """
    Get all libraries from jellyfin
    """
    get_library_result = get_virtual_folders.sync_detailed(client=client)
    match get_library_result.status_code:
        case 200:
            return Ok(get_library_result.parsed)  # type: ignore
        case _:
            return Err("Unknown error when getting api keys")


def create_library(client, name: str, library_type: CollectionTypeOptions, library_options: LibraryOptions, paths: list[str]) -> Result[None, str]:
    existing_libraries = get_libraries(client).expect("Failed to reach server")
    if name in [l.name for l in existing_libraries]:
        return Err("Library with same name already exists")
    if not all(validate_path.sync_detailed(client=client, body=ValidatePathDto(path=p)).status_code == 204 for p in paths):
        return Err("Invalid paths Provided")
    create_library_result = add_virtual_folder.sync_detailed(
        client=client, collection_type=library_type, body=AddVirtualFolderDto(library_options), paths=paths, refresh_library=True
    )
    # new_libraries = get_libraries(client).expect("Failed to reach server")

    return Ok(None) if create_library_result.status_code == 204 else Err(f"Unexpected response when creating library :{create_library_result.status_code}")


def delete_library(
    client,
    name: str,
):
    existing_libraries = get_libraries(client).expect("Failed to reach server")
    if name not in [l.name for l in existing_libraries]:
        return Err(f"Library {name} doesn't exist")
    delete_library_result = remove_virtual_folder.sync_detailed(client=client, name=name)
    return Ok(None) if delete_library_result.status_code == 204 else Err(f"Unexpected response when deleting library :{delete_library_result.status_code}")
