class PaymentModel {
  final String id;
  final String bookingId;
  final String farmerId;
  final String workerId;
  final double amount;
  final double platformCommission;
  final double workerPayout;
  final String status;
  final String? razorpayOrderId;
  final String? razorpayPaymentId;
  final String paymentMode;
  final String? paidAt;
  final String createdAt;

  PaymentModel({
    required this.id,
    required this.bookingId,
    required this.farmerId,
    required this.workerId,
    required this.amount,
    required this.platformCommission,
    required this.workerPayout,
    required this.status,
    this.razorpayOrderId,
    this.razorpayPaymentId,
    required this.paymentMode,
    this.paidAt,
    required this.createdAt,
  });

  factory PaymentModel.fromJson(Map<String, dynamic> json) => PaymentModel(
        id: json['id'] as String,
        bookingId: json['booking_id'] as String,
        farmerId: json['farmer_id'] as String,
        workerId: json['worker_id'] as String,
        amount: (json['amount'] as num).toDouble(),
        platformCommission: (json['platform_commission'] as num).toDouble(),
        workerPayout: (json['worker_payout'] as num).toDouble(),
        status: json['status'] as String,
        razorpayOrderId: json['razorpay_order_id'] as String?,
        razorpayPaymentId: json['razorpay_payment_id'] as String?,
        paymentMode: (json['payment_mode'] as String?) ?? 'UPI',
        paidAt: json['paid_at'] as String?,
        createdAt: json['created_at'] as String,
      );

  Map<String, dynamic> toJson() => {
        'id': id,
        'booking_id': bookingId,
        'farmer_id': farmerId,
        'worker_id': workerId,
        'amount': amount,
        'platform_commission': platformCommission,
        'worker_payout': workerPayout,
        'status': status,
        'razorpay_order_id': razorpayOrderId,
        'razorpay_payment_id': razorpayPaymentId,
        'payment_mode': paymentMode,
        'paid_at': paidAt,
        'created_at': createdAt,
      };
}
