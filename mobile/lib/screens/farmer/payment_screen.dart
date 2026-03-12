import 'package:flutter/material.dart';

class PaymentScreen extends StatelessWidget {
  const PaymentScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Payments / भुगतान')),
      body: const Center(child: Text('Razorpay checkout + payment history\n(TODO: Implement)')),
    );
  }
}
