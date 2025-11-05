subroutine iri20_init(direct)
    implicit none
    character(len=*), intent(in) :: direct
    call read_ig_rz(direct)
    call readapf107(direct)
end subroutine

subroutine iri20_eval(jf,jmag,alat,alon,iyyy,mmdd,dhour,zkm,nzkm,outf,oarr,direct,logfile)
    implicit none
    logical, intent(in) :: jf(50), jmag
    real, intent(in) :: alat, alon, dhour, zkm(nzkm), outf(20, nzkm), oarr(100)
    integer, intent(in) :: iyyy, mmdd, nzkm
    character, intent(in) :: direct(*)
    character, intent(in), optional :: logfile(*)
    call iri_sub(jf, jmag, alat, alon, iyyy, mmdd, dhour, zkm, nzkm, outf, oarr, direct,logfile)
end subroutine