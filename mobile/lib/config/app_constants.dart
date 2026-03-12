enum TaskType {
  sowing,
  transplanting,
  weeding,
  spraying,
  harvesting,
  threshing,
  loading,
  pruning,
  irrigation,
  other,
}

enum SkillType {
  sowing,
  transplanting,
  weeding,
  manualSpraying,
  machineSpraying,
  cottonPicking,
  grapeHarvesting,
  paddyHarvesting,
  sugarcaneCutting,
  tractorDriving,
  droneOperation,
  pruning,
  irrigation,
  loadingUnloading,
  other,
}

enum BookingStatus { pending, confirmed, checkedIn, completed, cancelled, noShow }

enum PaymentStatus { pending, heldInEscrow, released, refunded, failed }

enum UserRole { farmer, worker, contractor }

const Map<String, String> supportedLanguages = {
  'hi': 'हिंदी (Hindi)',
  'mr': 'मराठी (Marathi)',
  'gu': 'ગુજરાતી (Gujarati)',
  'pa': 'ਪੰਜਾਬੀ (Punjabi)',
  'ta': 'தமிழ் (Tamil)',
  'te': 'తెలుగు (Telugu)',
  'kn': 'ಕನ್ನಡ (Kannada)',
  'bn': 'বাংলা (Bengali)',
  'en': 'English',
};
