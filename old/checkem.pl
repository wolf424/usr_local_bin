#!/usr/bin/perl
# checkem.pl

use MD5;
require 'find.pl';

$md5 = new MD5;
@dirs = @ARGV;

foreach $dir ( @dirs ) { find($dir); }

sub wanted { push @files, $name; } # Cette sous-routine est appelée
                                   # pour chaque fichier trouvé

foreach $name ( sort @fles ) {
    ($uid,$gid) = (stat $name)[4,5];
    $stat = sprintf "%0o", (stat _)[2];
    unless ( -f $nam ) {
	printf "$stat\t$uid $gid\t\t\t\t\t\t$name\n";
	next;
    }
    # Effectuer une somme de contrôle
    $md5->reset();
    open FILE, $name or print(STDERR "Can't open file $name\n"), next;
    $md5->addfile(FILE);
    close FILE;

    $checksum = $md5->hexdigest();
    printf "$stat\t$uid $gid $checksum\t$name\n";
}
