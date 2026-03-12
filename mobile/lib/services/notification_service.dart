import 'package:firebase_messaging/firebase_messaging.dart';

class NotificationService {
  final FirebaseMessaging _messaging = FirebaseMessaging.instance;

  Future<void> initFCM() async {
    await requestPermission();
    FirebaseMessaging.onMessage.listen(_onMessage);
    FirebaseMessaging.onMessageOpenedApp.listen(_onMessageOpenedApp);
  }

  Future<void> requestPermission() async {
    await _messaging.requestPermission(
      alert: true,
      badge: true,
      sound: true,
    );
  }

  void _onMessage(RemoteMessage message) {
    // TODO: Show in-app notification banner
    print('[FCM] Message received: ${message.notification?.title}');
  }

  void _onMessageOpenedApp(RemoteMessage message) {
    // TODO: Navigate to relevant screen based on message data
    print('[FCM] App opened from notification: ${message.data}');
  }

  Future<String?> getToken() async {
    return await _messaging.getToken();
  }
}
