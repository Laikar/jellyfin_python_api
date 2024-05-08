from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="EncodingOptions")


@_attrs_define
class EncodingOptions:
    """
    Attributes:
        encoding_thread_count (Union[Unset, int]):
        transcoding_temp_path (Union[None, Unset, str]):
        fallback_font_path (Union[None, Unset, str]):
        enable_fallback_font (Union[Unset, bool]):
        down_mix_audio_boost (Union[Unset, float]):
        max_muxing_queue_size (Union[Unset, int]):
        enable_throttling (Union[Unset, bool]):
        throttle_delay_seconds (Union[Unset, int]):
        hardware_acceleration_type (Union[None, Unset, str]):
        encoder_app_path (Union[None, Unset, str]): Gets or sets the FFmpeg path as set by the user via the UI.
        encoder_app_path_display (Union[None, Unset, str]): Gets or sets the current FFmpeg path being used by the
            system and displayed on the transcode page.
        vaapi_device (Union[None, Unset, str]):
        enable_tonemapping (Union[Unset, bool]):
        enable_vpp_tonemapping (Union[Unset, bool]):
        tonemapping_algorithm (Union[None, Unset, str]):
        tonemapping_mode (Union[None, Unset, str]):
        tonemapping_range (Union[None, Unset, str]):
        tonemapping_desat (Union[Unset, float]):
        tonemapping_peak (Union[Unset, float]):
        tonemapping_param (Union[Unset, float]):
        vpp_tonemapping_brightness (Union[Unset, float]):
        vpp_tonemapping_contrast (Union[Unset, float]):
        h264_crf (Union[Unset, int]):
        h265_crf (Union[Unset, int]):
        encoder_preset (Union[None, Unset, str]):
        deinterlace_double_rate (Union[Unset, bool]):
        deinterlace_method (Union[None, Unset, str]):
        enable_decoding_color_depth_10_hevc (Union[Unset, bool]):
        enable_decoding_color_depth_10_vp_9 (Union[Unset, bool]):
        enable_enhanced_nvdec_decoder (Union[Unset, bool]):
        prefer_system_native_hw_decoder (Union[Unset, bool]):
        enable_intel_low_power_h264_hw_encoder (Union[Unset, bool]):
        enable_intel_low_power_hevc_hw_encoder (Union[Unset, bool]):
        enable_hardware_encoding (Union[Unset, bool]):
        allow_hevc_encoding (Union[Unset, bool]):
        enable_subtitle_extraction (Union[Unset, bool]):
        hardware_decoding_codecs (Union[List[str], None, Unset]):
        allow_on_demand_metadata_based_keyframe_extraction_for_extensions (Union[List[str], None, Unset]):
    """

    encoding_thread_count: Unset | int = UNSET
    transcoding_temp_path: None | Unset | str = UNSET
    fallback_font_path: None | Unset | str = UNSET
    enable_fallback_font: Unset | bool = UNSET
    down_mix_audio_boost: Unset | float = UNSET
    max_muxing_queue_size: Unset | int = UNSET
    enable_throttling: Unset | bool = UNSET
    throttle_delay_seconds: Unset | int = UNSET
    hardware_acceleration_type: None | Unset | str = UNSET
    encoder_app_path: None | Unset | str = UNSET
    encoder_app_path_display: None | Unset | str = UNSET
    vaapi_device: None | Unset | str = UNSET
    enable_tonemapping: Unset | bool = UNSET
    enable_vpp_tonemapping: Unset | bool = UNSET
    tonemapping_algorithm: None | Unset | str = UNSET
    tonemapping_mode: None | Unset | str = UNSET
    tonemapping_range: None | Unset | str = UNSET
    tonemapping_desat: Unset | float = UNSET
    tonemapping_peak: Unset | float = UNSET
    tonemapping_param: Unset | float = UNSET
    vpp_tonemapping_brightness: Unset | float = UNSET
    vpp_tonemapping_contrast: Unset | float = UNSET
    h264_crf: Unset | int = UNSET
    h265_crf: Unset | int = UNSET
    encoder_preset: None | Unset | str = UNSET
    deinterlace_double_rate: Unset | bool = UNSET
    deinterlace_method: None | Unset | str = UNSET
    enable_decoding_color_depth_10_hevc: Unset | bool = UNSET
    enable_decoding_color_depth_10_vp_9: Unset | bool = UNSET
    enable_enhanced_nvdec_decoder: Unset | bool = UNSET
    prefer_system_native_hw_decoder: Unset | bool = UNSET
    enable_intel_low_power_h264_hw_encoder: Unset | bool = UNSET
    enable_intel_low_power_hevc_hw_encoder: Unset | bool = UNSET
    enable_hardware_encoding: Unset | bool = UNSET
    allow_hevc_encoding: Unset | bool = UNSET
    enable_subtitle_extraction: Unset | bool = UNSET
    hardware_decoding_codecs: list[str] | None | Unset = UNSET
    allow_on_demand_metadata_based_keyframe_extraction_for_extensions: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        encoding_thread_count = self.encoding_thread_count

        transcoding_temp_path: None | Unset | str
        if isinstance(self.transcoding_temp_path, Unset):
            transcoding_temp_path = UNSET
        else:
            transcoding_temp_path = self.transcoding_temp_path

        fallback_font_path: None | Unset | str
        if isinstance(self.fallback_font_path, Unset):
            fallback_font_path = UNSET
        else:
            fallback_font_path = self.fallback_font_path

        enable_fallback_font = self.enable_fallback_font

        down_mix_audio_boost = self.down_mix_audio_boost

        max_muxing_queue_size = self.max_muxing_queue_size

        enable_throttling = self.enable_throttling

        throttle_delay_seconds = self.throttle_delay_seconds

        hardware_acceleration_type: None | Unset | str
        if isinstance(self.hardware_acceleration_type, Unset):
            hardware_acceleration_type = UNSET
        else:
            hardware_acceleration_type = self.hardware_acceleration_type

        encoder_app_path: None | Unset | str
        if isinstance(self.encoder_app_path, Unset):
            encoder_app_path = UNSET
        else:
            encoder_app_path = self.encoder_app_path

        encoder_app_path_display: None | Unset | str
        if isinstance(self.encoder_app_path_display, Unset):
            encoder_app_path_display = UNSET
        else:
            encoder_app_path_display = self.encoder_app_path_display

        vaapi_device: None | Unset | str
        if isinstance(self.vaapi_device, Unset):
            vaapi_device = UNSET
        else:
            vaapi_device = self.vaapi_device

        enable_tonemapping = self.enable_tonemapping

        enable_vpp_tonemapping = self.enable_vpp_tonemapping

        tonemapping_algorithm: None | Unset | str
        if isinstance(self.tonemapping_algorithm, Unset):
            tonemapping_algorithm = UNSET
        else:
            tonemapping_algorithm = self.tonemapping_algorithm

        tonemapping_mode: None | Unset | str
        if isinstance(self.tonemapping_mode, Unset):
            tonemapping_mode = UNSET
        else:
            tonemapping_mode = self.tonemapping_mode

        tonemapping_range: None | Unset | str
        if isinstance(self.tonemapping_range, Unset):
            tonemapping_range = UNSET
        else:
            tonemapping_range = self.tonemapping_range

        tonemapping_desat = self.tonemapping_desat

        tonemapping_peak = self.tonemapping_peak

        tonemapping_param = self.tonemapping_param

        vpp_tonemapping_brightness = self.vpp_tonemapping_brightness

        vpp_tonemapping_contrast = self.vpp_tonemapping_contrast

        h264_crf = self.h264_crf

        h265_crf = self.h265_crf

        encoder_preset: None | Unset | str
        if isinstance(self.encoder_preset, Unset):
            encoder_preset = UNSET
        else:
            encoder_preset = self.encoder_preset

        deinterlace_double_rate = self.deinterlace_double_rate

        deinterlace_method: None | Unset | str
        if isinstance(self.deinterlace_method, Unset):
            deinterlace_method = UNSET
        else:
            deinterlace_method = self.deinterlace_method

        enable_decoding_color_depth_10_hevc = self.enable_decoding_color_depth_10_hevc

        enable_decoding_color_depth_10_vp_9 = self.enable_decoding_color_depth_10_vp_9

        enable_enhanced_nvdec_decoder = self.enable_enhanced_nvdec_decoder

        prefer_system_native_hw_decoder = self.prefer_system_native_hw_decoder

        enable_intel_low_power_h264_hw_encoder = self.enable_intel_low_power_h264_hw_encoder

        enable_intel_low_power_hevc_hw_encoder = self.enable_intel_low_power_hevc_hw_encoder

        enable_hardware_encoding = self.enable_hardware_encoding

        allow_hevc_encoding = self.allow_hevc_encoding

        enable_subtitle_extraction = self.enable_subtitle_extraction

        hardware_decoding_codecs: list[str] | None | Unset
        if isinstance(self.hardware_decoding_codecs, Unset):
            hardware_decoding_codecs = UNSET
        elif isinstance(self.hardware_decoding_codecs, list):
            hardware_decoding_codecs = self.hardware_decoding_codecs

        else:
            hardware_decoding_codecs = self.hardware_decoding_codecs

        allow_on_demand_metadata_based_keyframe_extraction_for_extensions: list[str] | None | Unset
        if isinstance(self.allow_on_demand_metadata_based_keyframe_extraction_for_extensions, Unset):
            allow_on_demand_metadata_based_keyframe_extraction_for_extensions = UNSET
        elif isinstance(self.allow_on_demand_metadata_based_keyframe_extraction_for_extensions, list):
            allow_on_demand_metadata_based_keyframe_extraction_for_extensions = self.allow_on_demand_metadata_based_keyframe_extraction_for_extensions

        else:
            allow_on_demand_metadata_based_keyframe_extraction_for_extensions = self.allow_on_demand_metadata_based_keyframe_extraction_for_extensions

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if encoding_thread_count is not UNSET:
            field_dict["EncodingThreadCount"] = encoding_thread_count
        if transcoding_temp_path is not UNSET:
            field_dict["TranscodingTempPath"] = transcoding_temp_path
        if fallback_font_path is not UNSET:
            field_dict["FallbackFontPath"] = fallback_font_path
        if enable_fallback_font is not UNSET:
            field_dict["EnableFallbackFont"] = enable_fallback_font
        if down_mix_audio_boost is not UNSET:
            field_dict["DownMixAudioBoost"] = down_mix_audio_boost
        if max_muxing_queue_size is not UNSET:
            field_dict["MaxMuxingQueueSize"] = max_muxing_queue_size
        if enable_throttling is not UNSET:
            field_dict["EnableThrottling"] = enable_throttling
        if throttle_delay_seconds is not UNSET:
            field_dict["ThrottleDelaySeconds"] = throttle_delay_seconds
        if hardware_acceleration_type is not UNSET:
            field_dict["HardwareAccelerationType"] = hardware_acceleration_type
        if encoder_app_path is not UNSET:
            field_dict["EncoderAppPath"] = encoder_app_path
        if encoder_app_path_display is not UNSET:
            field_dict["EncoderAppPathDisplay"] = encoder_app_path_display
        if vaapi_device is not UNSET:
            field_dict["VaapiDevice"] = vaapi_device
        if enable_tonemapping is not UNSET:
            field_dict["EnableTonemapping"] = enable_tonemapping
        if enable_vpp_tonemapping is not UNSET:
            field_dict["EnableVppTonemapping"] = enable_vpp_tonemapping
        if tonemapping_algorithm is not UNSET:
            field_dict["TonemappingAlgorithm"] = tonemapping_algorithm
        if tonemapping_mode is not UNSET:
            field_dict["TonemappingMode"] = tonemapping_mode
        if tonemapping_range is not UNSET:
            field_dict["TonemappingRange"] = tonemapping_range
        if tonemapping_desat is not UNSET:
            field_dict["TonemappingDesat"] = tonemapping_desat
        if tonemapping_peak is not UNSET:
            field_dict["TonemappingPeak"] = tonemapping_peak
        if tonemapping_param is not UNSET:
            field_dict["TonemappingParam"] = tonemapping_param
        if vpp_tonemapping_brightness is not UNSET:
            field_dict["VppTonemappingBrightness"] = vpp_tonemapping_brightness
        if vpp_tonemapping_contrast is not UNSET:
            field_dict["VppTonemappingContrast"] = vpp_tonemapping_contrast
        if h264_crf is not UNSET:
            field_dict["H264Crf"] = h264_crf
        if h265_crf is not UNSET:
            field_dict["H265Crf"] = h265_crf
        if encoder_preset is not UNSET:
            field_dict["EncoderPreset"] = encoder_preset
        if deinterlace_double_rate is not UNSET:
            field_dict["DeinterlaceDoubleRate"] = deinterlace_double_rate
        if deinterlace_method is not UNSET:
            field_dict["DeinterlaceMethod"] = deinterlace_method
        if enable_decoding_color_depth_10_hevc is not UNSET:
            field_dict["EnableDecodingColorDepth10Hevc"] = enable_decoding_color_depth_10_hevc
        if enable_decoding_color_depth_10_vp_9 is not UNSET:
            field_dict["EnableDecodingColorDepth10Vp9"] = enable_decoding_color_depth_10_vp_9
        if enable_enhanced_nvdec_decoder is not UNSET:
            field_dict["EnableEnhancedNvdecDecoder"] = enable_enhanced_nvdec_decoder
        if prefer_system_native_hw_decoder is not UNSET:
            field_dict["PreferSystemNativeHwDecoder"] = prefer_system_native_hw_decoder
        if enable_intel_low_power_h264_hw_encoder is not UNSET:
            field_dict["EnableIntelLowPowerH264HwEncoder"] = enable_intel_low_power_h264_hw_encoder
        if enable_intel_low_power_hevc_hw_encoder is not UNSET:
            field_dict["EnableIntelLowPowerHevcHwEncoder"] = enable_intel_low_power_hevc_hw_encoder
        if enable_hardware_encoding is not UNSET:
            field_dict["EnableHardwareEncoding"] = enable_hardware_encoding
        if allow_hevc_encoding is not UNSET:
            field_dict["AllowHevcEncoding"] = allow_hevc_encoding
        if enable_subtitle_extraction is not UNSET:
            field_dict["EnableSubtitleExtraction"] = enable_subtitle_extraction
        if hardware_decoding_codecs is not UNSET:
            field_dict["HardwareDecodingCodecs"] = hardware_decoding_codecs
        if allow_on_demand_metadata_based_keyframe_extraction_for_extensions is not UNSET:
            field_dict["AllowOnDemandMetadataBasedKeyframeExtractionForExtensions"] = allow_on_demand_metadata_based_keyframe_extraction_for_extensions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        encoding_thread_count = d.pop("EncodingThreadCount", UNSET)

        def _parse_transcoding_temp_path(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        transcoding_temp_path = _parse_transcoding_temp_path(d.pop("TranscodingTempPath", UNSET))

        def _parse_fallback_font_path(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        fallback_font_path = _parse_fallback_font_path(d.pop("FallbackFontPath", UNSET))

        enable_fallback_font = d.pop("EnableFallbackFont", UNSET)

        down_mix_audio_boost = d.pop("DownMixAudioBoost", UNSET)

        max_muxing_queue_size = d.pop("MaxMuxingQueueSize", UNSET)

        enable_throttling = d.pop("EnableThrottling", UNSET)

        throttle_delay_seconds = d.pop("ThrottleDelaySeconds", UNSET)

        def _parse_hardware_acceleration_type(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        hardware_acceleration_type = _parse_hardware_acceleration_type(d.pop("HardwareAccelerationType", UNSET))

        def _parse_encoder_app_path(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        encoder_app_path = _parse_encoder_app_path(d.pop("EncoderAppPath", UNSET))

        def _parse_encoder_app_path_display(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        encoder_app_path_display = _parse_encoder_app_path_display(d.pop("EncoderAppPathDisplay", UNSET))

        def _parse_vaapi_device(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        vaapi_device = _parse_vaapi_device(d.pop("VaapiDevice", UNSET))

        enable_tonemapping = d.pop("EnableTonemapping", UNSET)

        enable_vpp_tonemapping = d.pop("EnableVppTonemapping", UNSET)

        def _parse_tonemapping_algorithm(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        tonemapping_algorithm = _parse_tonemapping_algorithm(d.pop("TonemappingAlgorithm", UNSET))

        def _parse_tonemapping_mode(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        tonemapping_mode = _parse_tonemapping_mode(d.pop("TonemappingMode", UNSET))

        def _parse_tonemapping_range(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        tonemapping_range = _parse_tonemapping_range(d.pop("TonemappingRange", UNSET))

        tonemapping_desat = d.pop("TonemappingDesat", UNSET)

        tonemapping_peak = d.pop("TonemappingPeak", UNSET)

        tonemapping_param = d.pop("TonemappingParam", UNSET)

        vpp_tonemapping_brightness = d.pop("VppTonemappingBrightness", UNSET)

        vpp_tonemapping_contrast = d.pop("VppTonemappingContrast", UNSET)

        h264_crf = d.pop("H264Crf", UNSET)

        h265_crf = d.pop("H265Crf", UNSET)

        def _parse_encoder_preset(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        encoder_preset = _parse_encoder_preset(d.pop("EncoderPreset", UNSET))

        deinterlace_double_rate = d.pop("DeinterlaceDoubleRate", UNSET)

        def _parse_deinterlace_method(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        deinterlace_method = _parse_deinterlace_method(d.pop("DeinterlaceMethod", UNSET))

        enable_decoding_color_depth_10_hevc = d.pop("EnableDecodingColorDepth10Hevc", UNSET)

        enable_decoding_color_depth_10_vp_9 = d.pop("EnableDecodingColorDepth10Vp9", UNSET)

        enable_enhanced_nvdec_decoder = d.pop("EnableEnhancedNvdecDecoder", UNSET)

        prefer_system_native_hw_decoder = d.pop("PreferSystemNativeHwDecoder", UNSET)

        enable_intel_low_power_h264_hw_encoder = d.pop("EnableIntelLowPowerH264HwEncoder", UNSET)

        enable_intel_low_power_hevc_hw_encoder = d.pop("EnableIntelLowPowerHevcHwEncoder", UNSET)

        enable_hardware_encoding = d.pop("EnableHardwareEncoding", UNSET)

        allow_hevc_encoding = d.pop("AllowHevcEncoding", UNSET)

        enable_subtitle_extraction = d.pop("EnableSubtitleExtraction", UNSET)

        def _parse_hardware_decoding_codecs(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                hardware_decoding_codecs_type_0 = cast(list[str], data)

                return hardware_decoding_codecs_type_0
            except:  # noqa: E722
                pass
            return cast(list[str] | None | Unset, data)

        hardware_decoding_codecs = _parse_hardware_decoding_codecs(d.pop("HardwareDecodingCodecs", UNSET))

        def _parse_allow_on_demand_metadata_based_keyframe_extraction_for_extensions(
            data: object,
        ) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allow_on_demand_metadata_based_keyframe_extraction_for_extensions_type_0 = cast(list[str], data)

                return allow_on_demand_metadata_based_keyframe_extraction_for_extensions_type_0
            except:  # noqa: E722
                pass
            return cast(list[str] | None | Unset, data)

        allow_on_demand_metadata_based_keyframe_extraction_for_extensions = _parse_allow_on_demand_metadata_based_keyframe_extraction_for_extensions(
            d.pop("AllowOnDemandMetadataBasedKeyframeExtractionForExtensions", UNSET)
        )

        encoding_options = cls(
            encoding_thread_count=encoding_thread_count,
            transcoding_temp_path=transcoding_temp_path,
            fallback_font_path=fallback_font_path,
            enable_fallback_font=enable_fallback_font,
            down_mix_audio_boost=down_mix_audio_boost,
            max_muxing_queue_size=max_muxing_queue_size,
            enable_throttling=enable_throttling,
            throttle_delay_seconds=throttle_delay_seconds,
            hardware_acceleration_type=hardware_acceleration_type,
            encoder_app_path=encoder_app_path,
            encoder_app_path_display=encoder_app_path_display,
            vaapi_device=vaapi_device,
            enable_tonemapping=enable_tonemapping,
            enable_vpp_tonemapping=enable_vpp_tonemapping,
            tonemapping_algorithm=tonemapping_algorithm,
            tonemapping_mode=tonemapping_mode,
            tonemapping_range=tonemapping_range,
            tonemapping_desat=tonemapping_desat,
            tonemapping_peak=tonemapping_peak,
            tonemapping_param=tonemapping_param,
            vpp_tonemapping_brightness=vpp_tonemapping_brightness,
            vpp_tonemapping_contrast=vpp_tonemapping_contrast,
            h264_crf=h264_crf,
            h265_crf=h265_crf,
            encoder_preset=encoder_preset,
            deinterlace_double_rate=deinterlace_double_rate,
            deinterlace_method=deinterlace_method,
            enable_decoding_color_depth_10_hevc=enable_decoding_color_depth_10_hevc,
            enable_decoding_color_depth_10_vp_9=enable_decoding_color_depth_10_vp_9,
            enable_enhanced_nvdec_decoder=enable_enhanced_nvdec_decoder,
            prefer_system_native_hw_decoder=prefer_system_native_hw_decoder,
            enable_intel_low_power_h264_hw_encoder=enable_intel_low_power_h264_hw_encoder,
            enable_intel_low_power_hevc_hw_encoder=enable_intel_low_power_hevc_hw_encoder,
            enable_hardware_encoding=enable_hardware_encoding,
            allow_hevc_encoding=allow_hevc_encoding,
            enable_subtitle_extraction=enable_subtitle_extraction,
            hardware_decoding_codecs=hardware_decoding_codecs,
            allow_on_demand_metadata_based_keyframe_extraction_for_extensions=allow_on_demand_metadata_based_keyframe_extraction_for_extensions,
        )

        return encoding_options
