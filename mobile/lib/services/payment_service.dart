import 'package:razorpay_flutter/razorpay_flutter.dart';

class PaymentService {
  late final Razorpay _razorpay;
  Function(PaymentSuccessResponse)? onSuccess;
  Function(PaymentFailureResponse)? onError;
  Function(ExternalWalletResponse)? onExternal;

  PaymentService() {
    _razorpay = Razorpay();
    _razorpay.on(Razorpay.EVENT_PAYMENT_SUCCESS, _handleSuccess);
    _razorpay.on(Razorpay.EVENT_PAYMENT_ERROR, _handleError);
    _razorpay.on(Razorpay.EVENT_EXTERNAL_WALLET, _handleExternal);
  }

  void openCheckout({
    required String orderId,
    required double amount,
    required String name,
    required String description,
    required String phone,
  }) {
    final options = {
      'key': 'rzp_test_YOUR_KEY',
      'amount': (amount * 100).toInt(),
      'order_id': orderId,
      'name': 'FarmForce AI',
      'description': description,
      'prefill': {'contact': phone},
    };
    _razorpay.open(options);
  }

  void _handleSuccess(PaymentSuccessResponse response) {
    onSuccess?.call(response);
  }

  void _handleError(PaymentFailureResponse response) {
    onError?.call(response);
  }

  void _handleExternal(ExternalWalletResponse response) {
    onExternal?.call(response);
  }

  void dispose() {
    _razorpay.clear();
  }
}
