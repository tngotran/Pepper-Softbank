<?xml version="1.0" encoding="UTF-8" ?>
<Package name="PepperMusio" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="HelloWorld2" src="HelloWorld2/HelloWorld2.dlg" />
    </Dialogs>
    <Resources />
    <Topics>
        <Topic name="HelloWorld2_enu" src="HelloWorld2/HelloWorld2_enu.top" topicName="HelloWorld2" language="en_US" />
    </Topics>
    <IgnoredPaths>
        <Path src="testMusioServer.py" />
    </IgnoredPaths>
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
