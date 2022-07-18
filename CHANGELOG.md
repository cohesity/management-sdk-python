# [1.8.1] - 2022-07-08
Paatch release with updated .py files.

### Added
- None

### Changed
- Updated python files where dict.get("field") is used instead
of dictionary.get("field")

### Fixed
- None

### Removed
- None

# [1.8.0] - 2021-12-23
New SDK release for Cluster 6.6.0d

### Added
- None

### Changed
- Updated SDK with new modules and functions added in 6.6.0d V1 version.

### Fixed
- None

### Removed
- None

# [1.7.0] - 2021-08-18
Paatch release with updated requirements

### Added
- None

### Changed
- Removed jsonpickle dependency, replaced with Json.

### Fixed
- None

### Removed
- None

# [1.6.0] - 2021-02-22
New SDK for Cluster 6.6

### Added
- None

### Changed
- None

### Fixed
- None

### Removed
- None

# [1.5.2] - 2021-01-15
Patch release for blackout policy issue fix

### Added
- None

### Changed
- None

### Fixed
- Fixed code for blackout policy issue.

### Removed
- None

# [1.5.1] - 2020-09-11
Patch release for query params issue.

### Added
- None

### Changed
- None

### Fixed
- Fixed code to update the query params as a list of comma separated values.

### Removed
- None

# [1.5.0] - 2020-09-01
New version of Cohesity Management SDK is here!

### Added
- Added support for LTS 6.5.1x Cohesity DataPlatform.

### Changed
- None

### Fixed
- None

### Removed
- None

# [1.4.0] - 2020-09-01
New version of Cohesity Management SDK is here!

### Added
- Added support for LTS 6.5.0x Cohesity DataPlatform.

### Changed
- None

### Fixed
- None

### Removed
- None

# [1.2.1] - 2020-03-09
Patch release for exception handling fix

### Added
- None

### Changed
- None

### Fixed
- Issue #13:  Exception handling revered back to `raise` instead of `raise APIException`

### Removed
- None

# [1.2.0] - 2020-02-03
New version of Cohesity Management SDK is here!

### Added
- Added support for LTS 6.4.1x Cohesity DataPlatform.

### Changed
- None

### Fixed
- None

### Removed
- None

# [1.1.3] - 2019-11-05
New version of Cohesity Management SDK is here!

### Added
- Added support for LTS 6.3.1x Cohesity DataPlatform.

### Changed
- None

### Fixed
- None

### Removed
- None

# [1.1.2] - 2019-08-12
New version of Cohesity Management SDK is here!

### Added
- ~40 endpoints supported in  6.4 have been added  

### Changed
- None

### Fixed
 None

### Removed
- None


# [1.1.1] - 2019-08-05
New version of Cohesity Management SDK is here!

### Added
- This SDK now supports Cohesity DataPlatform 6.4

### Changed
- Minor bug fixes for some model names.
### Fixed
- Fixed the issue #6 . Creating vlan is now possible through python sdk.

### Removed
- None.



# [1.1.0] - 2019-06-20
Yay! New version of Cohesity Management SDK is here!

### Added 
- This SDK now supports Cohesity DataPlatform 6.3

### Changed
- (BREAKING CHANGE) Models names have changed because the way we genereated the models was not consistent. We did to ensure future versions of the SDK are 100% backward compatible. 

### Fixed
- None
 
### Removed
- Tenants controller(tenants_controller.py) is removed, now all the endpoints related to tenants are in tenant_controller.py

