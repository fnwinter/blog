---
layout: post
title: "outlook eml import"
author: "jungjik.lee"
categories: article
tags: [eml, outlook, office]
---

# :email: 아웃룩 eml 백업
- 어쩌다가 옛날 이메일을 다 eml 파일로 백업을 해 놓았는데, 이걸 다시 :mailbox: 아웃룩으로 복구할 방법을 찾다가, 아래 링크의 사이트를 발견하게 되었다.
- https://www.howto-outlook.com/howto/import-eml-files.htm?utm_source=pocket_mylist
- VB 스크립트로 아웃룩을 띄어 놓고 eml 파일 하나씩 오픈하면서 다시 아웃룩에 Move to 하는 방법인데, 문제는 스크립트에 오류가 하나 있다.
- 그래서 이번 포스트는 그 버그 픽스를 남겨 놓을려고 한다.
    <pre><code>
    Dim objShell : Set objShell = CreateObject("Shell.Application")
    Dim objFolder : Set objFolder = objShell.BrowseForFolder(0, "Select the folder containing eml-files", 0)

    Dim Item
    Dim i : i = 0
    If (NOT objFolder is Nothing) Then
    Set WShell = CreateObject("WScript.Shell")
    Set objOutlook = CreateObject("Outlook.Application")
    Set Folder = objOutlook.Session.PickFolder
    If NOT Folder Is Nothing Then
        For Each Item in objFolder.Items
        If Right(Item.Path, 4) = ".eml" AND Item.IsFolder = False Then
        objShell.ShellExecute Item.Path, "", "", "open", 1
        WScript.Sleep 500
        Set MyInspector = objOutlook.ActiveInspector
        Set MyItem = objOutlook.ActiveInspector.CurrentItem
        MyItem.Move Folder
        i = i + 1
        End If
        Next

        MsgBox "Import completed." & vbNewLine & vbNewLine & "Imported eml-files: " & i & _
        vbNewLine & "Imported into: " & Folder.FolderPath, 64, "Import EML"

        Set Folder = Nothing
    Else
        MsgBox "Import canceled.", 64, "Import EML"
    End If
    Else
    MsgBox "Import canceled.", 64, "Import EML"
    End If

    Set objFolder = Nothing
    Set objShell = Nothing
    </code></pre>
- 위 코드를 import_eml.vb 로 저장하고 아웃룩을 실행한 다음, import_eml.vb를 실행하고 메일이 있는 폴더와 저장하고자 하는 아웃룩 폴더를 지정하면 자동으로 import 된다.
