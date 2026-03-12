import 'package:flutter/material.dart';

class VoiceInputButton extends StatefulWidget {
  final VoidCallback onStart;
  final VoidCallback onStop;

  const VoiceInputButton({super.key, required this.onStart, required this.onStop});

  @override
  State<VoiceInputButton> createState() => _VoiceInputButtonState();
}

class _VoiceInputButtonState extends State<VoiceInputButton> with SingleTickerProviderStateMixin {
  bool _isRecording = false;
  late AnimationController _controller;
  late Animation<double> _animation;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 800))..repeat(reverse: true);
    _animation = Tween<double>(begin: 0.9, end: 1.1).animate(_controller);
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {
        setState(() => _isRecording = !_isRecording);
        if (_isRecording) widget.onStart(); else widget.onStop();
      },
      child: ScaleTransition(
        scale: _isRecording ? _animation : const AlwaysStoppedAnimation(1.0),
        child: Container(
          width: 64,
          height: 64,
          decoration: BoxDecoration(
            color: _isRecording ? Colors.red : const Color(0xFF2E7D32),
            shape: BoxShape.circle,
          ),
          child: Icon(_isRecording ? Icons.stop : Icons.mic, color: Colors.white, size: 32),
        ),
      ),
    );
  }
}
