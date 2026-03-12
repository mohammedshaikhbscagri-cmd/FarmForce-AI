import 'package:flutter/material.dart';

class FarmerProfileScreen extends StatelessWidget {
  const FarmerProfileScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('My Profile / मेरी प्रोफाइल')),
      body: const Center(child: Text('Farmer profile + farms + settings\n(TODO: Implement)')),
    );
  }
}
