import 'package:speech_to_text/speech_to_text.dart';

class VoiceService {
  final SpeechToText _speechToText = SpeechToText();
  bool _isInitialized = false;
  String _transcription = '';

  Future<void> initialize() async {
    _isInitialized = await _speechToText.initialize();
  }

  Future<void> startListening({String locale = 'hi-IN'}) async {
    if (!_isInitialized) await initialize();
    if (_speechToText.isAvailable) {
      _transcription = '';
      await _speechToText.listen(
        onResult: (result) => _transcription = result.recognizedWords,
        localeId: locale,
      );
    }
  }

  Future<void> stopListening() async {
    await _speechToText.stop();
  }

  String getTranscription() => _transcription;

  bool get isListening => _speechToText.isListening;

  void dispose() {
    _speechToText.cancel();
  }
}
