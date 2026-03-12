import 'package:hive_flutter/hive_flutter.dart';

class OfflineService {
  static const String _jobsBoxName = 'jobs_cache';
  static const String _bookingsBoxName = 'bookings_cache';

  Future<void> saveToLocal(String boxName, String key, dynamic value) async {
    final box = await Hive.openBox(boxName);
    await box.put(key, value);
  }

  Future<dynamic> loadFromLocal(String boxName, String key) async {
    final box = await Hive.openBox(boxName);
    return box.get(key);
  }

  Future<void> saveJobs(List<Map<String, dynamic>> jobs) async {
    await saveToLocal(_jobsBoxName, 'jobs', jobs);
  }

  Future<List<Map<String, dynamic>>?> loadJobs() async {
    final data = await loadFromLocal(_jobsBoxName, 'jobs');
    if (data == null) return null;
    return List<Map<String, dynamic>>.from(data as List);
  }

  Future<void> saveBookings(List<Map<String, dynamic>> bookings) async {
    await saveToLocal(_bookingsBoxName, 'bookings', bookings);
  }

  Future<void> syncWithServer() async {
    // TODO: Implement background sync logic
    // 1. Check network availability
    // 2. Fetch latest data from server
    // 3. Merge with local changes
    print('[OfflineService] Syncing with server...');
  }
}
